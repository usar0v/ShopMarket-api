# Generated by Django 3.2.9 on 2021-11-28 10:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_product_colors'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=5),
        ),
    ]