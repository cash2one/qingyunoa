# coding=utf-8
from django.apps import AppConfig

__author__ = 'lyhapple'


class CRMAppConfig(AppConfig):
    name = "apps.crm"
    verbose_name = u"客户关系管理"

    def ready(self):
        import serializers
        pass
