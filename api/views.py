from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Mini_category, Product
from .serializers import CategorySerializer, Mini_CategorySerializer, ProductSerializer, UserSerializer


class CategoryView(APIView):
  def get(self, request, pk=None, format=None):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

  def post(self, request, pk=None, format=None):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response('Data Created')
    return Response(serializer.errors)


class Mini_categoryView(APIView):
  def get(self, request, pk=None, format=None):
    mini_category = Mini_category.objects.all()
    serializer = Mini_CategorySerializer(mini_category, many=True)
    return Response(serializer.data)

  def post(self, request, pk=None, format=None):
    serializer = Mini_CategorySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response('Data Created')
    return Response(serializer.errors)


class ProductView(APIView):
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      product = Product.objects.get(id=id)
      serializer = ProductSerializer(product)
      Response(serializer.data)

    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

  def post(self, request, pk=None, format=None):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)

  def put(self, request, pk=None, format=None):
    id = pk
    product = Product.objects.get(pk=id)
    serializer = ProductSerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)

  def delete(self, request, pk=None, format=None):
    id = pk
    product = Product.objects.get(id=id)
    product.delete()
    return Response('Data Deleted')


class UserView(APIView):
  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      product = User.objects.get(id=id)
      serializer = UserSerializer(product)
      Response(serializer.data)

    product = User.objects.all()
    serializer = UserSerializer(product, many=True)
    return Response(serializer.data)

  def post(self, request, pk=None, format=None):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)
