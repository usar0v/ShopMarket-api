from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Category, Mini_category, Product


class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model = Category
    fields = ('id', 'title')


class Mini_CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Mini_category
    fields = ('id', 'title', 'category')


class ProductSerializer(serializers.ModelSerializer):
  # created_by = serializers.ReadOnlyField(source='created_by.username', read_only=False)
  class Meta:
    model = Product
    fields = ('id', 'title', 'mini_category', 'brand', 'price', 'image', 'colors', 'sizes', 'status', 'created_by', 'date_created',)


class UserSerializer(serializers.ModelSerializer):
  products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'date_joined', 'products']