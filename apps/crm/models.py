# coding=utf-8

from django.db import models
from core.adminlte.models import BaseModel, SystemConfig


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