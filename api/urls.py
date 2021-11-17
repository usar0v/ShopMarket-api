from django.urls import path

from .views import CategoryView, Mini_categoryView, ProductView, UserView

urlpatterns = [
  path('categories', CategoryView.as_view()),

  path('mini_categories', Mini_categoryView.as_view()),

  path('products/', ProductView.as_view()),
  path('products/<int:pk>', ProductView.as_view()),

  path('users', UserView.as_view()),
]
