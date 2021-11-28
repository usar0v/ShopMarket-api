from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.fields import ListField
from .models import Category, Mini_category, Product


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('id', 'name')


class Mini_CategorySerializer(serializers.ModelSerializer):
  # category = serializers.CharField()
  products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

  class Meta:
    model = Mini_category
    fields = ('id', 'name', 'category', 'products')

  # def create(self, validated_data):
  #   category = validated_data.pop('category')
  #   category_instance, created = Category.objects.get_or_create(name=category)
  #   mini_category_instance = Mini_category.objects.create(**validated_data, category=category_instance)
  #   return mini_category_instance


class StringArrayField(ListField):
  """
  String representation of an array field.
  """

  def to_representation(self, obj):
    obj = super().to_representation(obj)
    # convert list to string
    return ",".join([str(element) for element in obj])

  def to_internal_value(self, data):
    for line in data:
      data = line.split(",")  # convert string to list
      return super().to_internal_value(data)


class ProductSerializer(serializers.ModelSerializer):
  # mini_category = serializers.IntegerField()
  # colors = StringArrayField
  colors = serializers.ListField()

  class Meta:
    model = Product
    fields = (
    'id', 'title', 'mini_category', 'category', 'brand', 'price', 'rating', 'image', 'colors', 'status', 'created_by',
    'sizes', 'discount', 'date_created')

  # def create(self, validated_data):
  #   mini_category = validated_data.pop('mini_category')
  #   model_mini_category = Mini_category.objects.filter(name=mini_category).count()
  #   mini_category_instance, created = model_mini_category.objects.get_or_create(name=mini_category)
  #   product_instance = Product.objects.create(**validated_data, mini_category=mini_category_instance)
  #   return product_instance


class UserSerializer(serializers.ModelSerializer):
  products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'date_joined', 'products']
