from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework_simplejwt.tokens import AccessToken, RefreshToken, UntypedToken

from .cart.serializers import CartSerializer
from www import models


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Choice
        fields = '__all__'


class ChoiceTypeSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = models.ChoiceType
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    choice_types = ChoiceTypeSerializer(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = models.Category
        fields = '__all__'


class OrderItemChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItemChoice
        fields = '__all__'
        read_only_fields = ['order_item']


class OrderItemSerializer(serializers.ModelSerializer):
    order_item_choices = OrderItemChoiceSerializer(many=True, required=False)

    class Meta:
        model = models.OrderItem
        fields = '__all__'
        read_only_fields = ['order']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, required=False)

    class Meta:
        model = models.Order
        fields = '__all__'
        read_only = ['date', 'state']

    def create(self, validated_data):
        order_items = validated_data.pop('order_items')
        order = models.Order.objects.create(**validated_data)
        for order_item_data in order_items:
            order_item_choices = order_item_data.pop('order_item_choices')
            order_item = models.OrderItem.objects.create(
                order=order, **order_item_data)
            for order_item_choice_data in order_item_choices:
                models.OrderItemChoice.objects.create(
                    order_item=order_item, **order_item_choice_data)
        return order


class CustomerSerializer(serializers.ModelSerializer):
    cart = CartSerializer()

    class Meta:
        model = models.Customer
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'token', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])

        user = super(RegisterSerializer, self).create(validated_data=validated_data)

        customer = models.Customer(
            user=user, username=validated_data['username'])

        customer.save()

        return user

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data
