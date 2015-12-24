# coding=utf-8
from django.core.urlresolvers import reverse

from django.db import models
from core.adminlte.constants import DICT_NULL_BLANK_TRUE, UsableStatus
from core.adminlte.models import BaseModel, SystemConfig
from core.organization.models import Staff, AbstractPersonInfo


class Product(BaseModel):
    """
    产品模型
    """
    name = models.CharField(
        verbose_name=u'名称', max_length=100
    )
    status = models.ForeignKey(
        SystemConfig,
        related_name='+',
        verbose_name=u'状态',
        db_index=True,
        limit_choices_to={'parent__name': 'product_status'}
    )
    ptype = models.ForeignKey(
        SystemConfig,
        related_name='+',
        verbose_name=u'类型',
        db_index=True,
        limit_choices_to={'parent__name': 'product_type'}
    )

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'adminlte:common_detail_page',
            kwargs={
                'app_name': self._meta.app_label,
                'model_name': self._meta.model_name,
                'pk': self.id
            }
        )

    class Meta:
        verbose_name_plural = verbose_name = u'产品'

    class Config:
        list_display_fields = ('name', 'status', 'ptype', 'id')
        list_form_fields = list_display_fields
        search_fields = ('name',)
        filter_fields = list_display_fields


class Customer(BaseModel):
    """
    客户模型
    """
    name = models.CharField(
        verbose_name=u'名称', max_length=200
    )
    assign_to = models.ForeignKey(
        Staff,
        verbose_name=u'指派',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )
    grade = models.ForeignKey(
        SystemConfig,
        related_name='+',
        limit_choices_to={'parent__name': 'customer_grade'},
        verbose_name=u'等级',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )
    status = models.ForeignKey(
        SystemConfig,
        related_name='+',
        limit_choices_to={'parent__name': 'customer_status'},
        verbose_name=u'状态',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )
    scale = models.ForeignKey(
        SystemConfig,
        related_name='+',
        limit_choices_to={'parent__name': 'customer_scale'},
        verbose_name=u'规模',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )
    ctype = models.ForeignKey(
        SystemConfig,
        related_name='+',
        limit_choices_to={'parent__name': 'customer_type'},
        verbose_name=u'类型',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )
    last_contact_date = models.DateField(
        verbose_name=u'最后联系',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )
    next_contact_date = models.DateField(
        verbose_name=u'下次联系',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'adminlte:common_detail_page',
            kwargs={
                'app_name': self._meta.app_label,
                'model_name': self._meta.model_name,
                'pk': self.id
            }
        )

    @staticmethod
    def update_contact_date(customer, last_date, next_date):
        """
        更新联系时间
        :param customer: 客户实例
        :param last_date: 最后联系时间
        :param next_date: 下次联系时间
        """
        customer.last_contact_date = last_date
        customer.next_contact_date = next_date
        customer.save()

    class Meta:
        verbose_name_plural = verbose_name = u'客户'

    class Config:
        list_display_fields = ('name', 'assign_to', 'scale', 'ctype', 'status',
                               'grade', 'last_contact_time',
                               'next_contact_time', 'id')
        list_form_fields = ('name', 'assign_to',
                            'scale', 'ctype', 'status',
                            'grade')


class Contact(AbstractPersonInfo):
    """
    联系人模型
    """
    customer = models.ForeignKey(
        Customer,
        related_name='+',
        verbose_name=u'所属客户',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )
    department = models.CharField(
        verbose_name=u'部门',
        max_length=200,
        default='',
        **DICT_NULL_BLANK_TRUE
    )
    fax = models.CharField(
        verbose_name=u'传真',
        max_length=20,
        default='',
        **DICT_NULL_BLANK_TRUE
    )
    note = models.TextField(
        verbose_name=u'备注',
        default='',
        **DICT_NULL_BLANK_TRUE
    )

    def __unicode__(self):
        return self.real_name

    class Meta:
        verbose_name_plural = verbose_name = u'联系人'

    class Config:
        list_display_fields = ('real_name', 'customer', 'position',
                               'cellphone', 'email', 'qq', 'id')
        list_form_fields = list_display_fields + ('sex', 'job_status',
                                                  'birthday', 'location', )
        filter_fields = ('status', )
        search_fields = ('real_name', 'cellphone')


class Order(BaseModel, UsableStatus):
    """
    订单模型
    """
    customer = models.ForeignKey(
        Customer,
        related_name='+',
        verbose_name=u'所属客户',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )
    product = models.ForeignKey(
        Product,
        related_name='+',
        verbose_name=u'产品',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )
    assign_to = models.ForeignKey(
        Staff,
        verbose_name=u'指派给',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )
    plan_amount = models.FloatField(
        verbose_name=u'计划金额(RMB)',
        default=0.0,
    )
    deal_amount = models.FloatField(
        verbose_name=u'成交金额(RMB)',
        default=0.0
    )
    last_contact_date = models.DateField(
        verbose_name=u'最后联系',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )
    next_contact_date = models.DateField(
        verbose_name=u'下次联系',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )
    order_status = models.ForeignKey(
        SystemConfig,
        verbose_name=u'状态',
        related_name='+',
        limit_choices_to={'parent__name': 'order_status'}
    )
    status = models.PositiveSmallIntegerField(
        u'数据状态', choices=UsableStatus.STATUS,
        default=UsableStatus.USABLE
    )

    def __unicode__(self):
        return u'%s购买%s' % (self.customer.name, self.product.name)

    class Meta:
        verbose_name_plural = verbose_name = u'订单'

    class Config:
        list_display_fields = (
            'customer', 'product', 'plan_amount', 'deal_amount', 'assign_to',
            'order_status', 'id'
        )
        list_form_fields = list_display_fields
        search_fields = ('customer', 'product', )
        filter_fields = search_fields


class Contract(BaseModel, UsableStatus):
    order = models.ForeignKey(
        Order,
        verbose_name=u'所属订单',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )
    number = models.CharField(
        verbose_name=u'合同编号',
        max_length=200,
        default='',
        **DICT_NULL_BLANK_TRUE
    )
    amount = models.FloatField(
        verbose_name=u'合同金额',
        default=0.0,
        **DICT_NULL_BLANK_TRUE
    )
    start_date = models.DateField(
        verbose_name=u'开始日期'
    )
    end_date = models.DateField(
        verbose_name=u'结束日期'
    )
    pay_status = models.ForeignKey(
        SystemConfig,
        limit_choices_to={'parent__name': 'pay_status'},
        verbose_name=u'付款状态',
        related_name='+',
        **DICT_NULL_BLANK_TRUE
    )
    delivery_status = models.ForeignKey(
        SystemConfig,
        limit_choices_to={'parent__name': 'delivery_status'},
        verbose_name=u'交付状态',
        related_name='+',
        **DICT_NULL_BLANK_TRUE
    )
    contract_status = models.ForeignKey(
        SystemConfig,
        limit_choices_to={'parent__name': 'contract_status'},
        verbose_name=u'合同状态',
        related_name='+',
        **DICT_NULL_BLANK_TRUE
    )
    status = models.PositiveSmallIntegerField(
        u'数据状态', choices=UsableStatus.STATUS,
        default=UsableStatus.USABLE
    )

    def __unicode__(self):
        return u'%s(%s)' % (self.number, self.order)

    def get_absolute_url(self):
        return reverse(
            'adminlte:common_detail_page',
            kwargs={
                'app_name': self._meta.app_label,
                'model_name': self._meta.model_name,
                'pk': self.id
            }
        )

    class Meta:
        verbose_name_plural = verbose_name = u'合同'

    class Config:
        list_display_fields = ('order', 'number', 'amount', 'start_date',
                               'end_date', 'pay_status', 'delivery_status',
                               'contract_status', 'id')
        list_form_fields = list_display_fields
        search_fields = ('number', )
        filter_fields = search_fields
