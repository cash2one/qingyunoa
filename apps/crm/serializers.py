# coding=utf-8
from rest_framework import serializers
from .models import Product, Customer

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


class CustomerSerializer(serializers.ModelSerializer):
    ctype = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    scale = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()
    assign_to = serializers.SerializerMethodField()

    def get_ctype(self, obj):
        return obj.ctype.value

    def get_status(self, obj):
        return obj.status.value

    def get_scale(self, obj):
        return obj.scale.title

    def get_grade(self, obj):
        return obj.grade.name

    def get_assign_to(self, obj):
        return obj.assign_to.real_name

    class Meta:
        model = Customer
        fields = Customer.Config.list_display_fields
        read_only_fields = ('id', )
