# coding=utf-8
from rest_framework import serializers
from .models import Product, Customer, Contact, Order, Contract

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


class ContactSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()

    def get_customer(self, obj):
        return '<a href="%s">%s</a>' % (obj.customer.get_absolute_url(),
                                        obj.customer.name)

    def get_position(self, obj):
        return obj.get_position_display()

    class Meta:
        model = Contact
        fields = Contact.Config.list_display_fields
        read_only_fields = ('id', )


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()
    order_status = serializers.SerializerMethodField()
    assign_to = serializers.SerializerMethodField()

    def get_order_status(self, obj):
        return obj.order_status.value

    def get_assign_to(self, obj):
        return '<a href="%s">%s</a>' % (obj.assign_to.get_absolute_url(),
                                        obj.assign_to.real_name)

    def get_customer(self, obj):
        return '<a href="%s">%s</a>' % (obj.customer.get_absolute_url(),
                                        obj.customer.name)

    def get_product(self, obj):
        return '<a href="%s">%s</a>' % (obj.product.get_absolute_url(),
                                        obj.product.name)

    class Meta:
        model = Order
        fields = Order.Config.list_display_fields
        read_only_fields = ('id', )


class ContractSerializer(serializers.ModelSerializer):
    order = serializers.SerializerMethodField()
    pay_status = serializers.SerializerMethodField()
    delivery_status = serializers.SerializerMethodField()
    contract_status = serializers.SerializerMethodField()

    def get_pay_status(self, obj):
        return obj.pay_status.value

    def get_delivery_status(self, obj):
        return obj.delivery_status.value

    def get_contract_status(self, obj):
        return obj.contract_status.value

    def get_order(self, obj):
        return obj.order.__unicode__()

    class Meta:
        model = Contract
        fields = Contract.Config.list_display_fields
        read_only_fields = ('id', )