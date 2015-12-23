# coding=utf-8
from rest_framework import serializers
from .models import Product

__author__ = 'lyhapple'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = Product.Config.list_display_fields
        read_only_fields = ('id', )
