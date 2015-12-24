# coding=utf-8
from rest_framework import serializers
from .models import Product

__author__ = 'lyhapple'


class ProductSerializer(serializers.ModelSerializer):
    ptype = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def get_ptype(self, obj):
        return obj.ptype.value

    def get_status(self, obj):
        return obj.status.value

    class Meta:
        model = Product
        fields = Product.Config.list_display_fields
        read_only_fields = ('id', )
