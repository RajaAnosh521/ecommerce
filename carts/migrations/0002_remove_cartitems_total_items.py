# Generated by Django 5.1 on 2024-08-11 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='total_items',
        ),
    ]
