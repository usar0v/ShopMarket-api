from django.contrib.postgres.fields import ArrayField
from django.db import models


class Category(models.Model):
  title = models.CharField(max_length=55, unique=True)

  def __str__(self):
    return self.title


class Mini_category(models.Model):
  title = models.CharField(max_length=150, unique=True)
  category = models.ForeignKey(Category, related_name='mini_categories', on_delete=models.CASCADE)

  def __str__(self):
    return self.title


class Product(models.Model):
  brand = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  mini_category = models.ForeignKey(Mini_category, null=True, related_name='sezons', on_delete=models.CASCADE)
  price = models.IntegerField()
  image = models.ImageField(upload_to='picture/', height_field=None, width_field=None, max_length=100,
                              default='default.jpg')
  colors = ArrayField(models.CharField(max_length=20, null=True, blank=True), size=8)
  created_by = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE, null=True)
  sizes = ArrayField(models.IntegerField(null=True, blank=True), size=8)
  status = models.BooleanField(default=True)
  date_created = models.DateField(auto_now_add=True)



  def __str__(self):
    return '{} {}'.format(self.brand, self.title)

