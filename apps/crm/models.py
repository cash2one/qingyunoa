# coding=utf-8

from django.db import models
from core.adminlte.constants import DICT_NULL_BLANK_TRUE
from core.adminlte.models import BaseModel, SystemConfig
from core.organization.models import Staff


class Product(BaseModel):
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

    class Meta:
        verbose_name_plural = verbose_name = u'产品'

    class Config:
        list_display_fields = ('name', 'status', 'ptype', 'id')
        list_form_fields = list_display_fields
        search_fields = ('name',)
        filter_fields = list_display_fields


class Customer(BaseModel):
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
    last_contact_time = models.DateTimeField(
        verbose_name=u'最后联系时间',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )
    next_contact_time = models.DateTimeField(
        verbose_name=u'最后联系时间',
        default=None,
        **DICT_NULL_BLANK_TRUE
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = u'客户'

    class Config:
        list_display_fields = ('name', 'assign_to', 'scale', 'ctype', 'status',
                               'grade', 'last_contact_time',
                               'next_contact_time', 'id')
        list_form_fields = ('name', 'assign_to',
                            'scale', 'ctype', 'status',
                            'grade')