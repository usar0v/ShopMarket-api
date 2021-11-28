from django.contrib.postgres.fields import ArrayField
from django.db import models


class Category(models.Model):
  name = models.CharField(max_length=55, unique=True)

  def __str__(self):
    return self.name


class Mini_category(models.Model):
  name = models.CharField(max_length=150)
  category = models.ForeignKey(Category, related_name='mini_categories', on_delete=models.CASCADE)

  def __str__(self):
    return self.name


class Product(models.Model):
  brand = models.CharField(max_length=50, null=True)
  title = models.CharField(max_length=50)
  category = models.ForeignKey(Category, related_name='products_category', null=True, on_delete=models.CASCADE)
  mini_category = models.ForeignKey(Mini_category, null=True, related_name='products', on_delete=models.CASCADE)
  price = models.IntegerField()
  image = models.ImageField(upload_to='picture/', height_field=None, width_field=None, max_length=100,
                              default='default.jpg')
  colors = ArrayField(models.CharField(max_length=20), size=5, default=[])
  sizes = ArrayField(models.CharField(max_length=10), size=5, default=list)
  created_by = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE, null=True)
  rating = models.IntegerField(default=5)
  status = models.BooleanField(default=True)
  discount = models.IntegerField(null=True)
  date_created = models.DateField(auto_now_add=True)



  def __str__(self):
    return '{} {}'.format(self.brand, self.title)

