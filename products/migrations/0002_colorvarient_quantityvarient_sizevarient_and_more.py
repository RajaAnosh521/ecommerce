# Generated by Django 5.1 on 2024-08-09 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorVarient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=100)),
                ('color_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QuantityVarient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('varient_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SizeVarient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='color_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.colorvarient'),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.quantityvarient'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.sizevarient'),
        ),
    ]
