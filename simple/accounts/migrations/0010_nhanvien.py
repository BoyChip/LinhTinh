# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-13 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_hang'),
    ]

    operations = [
        migrations.CreateModel(
            name='NhanVien',
            fields=[
                ('MaNhanVien', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('TenNhanVien', models.CharField(max_length=50)),
                ('DiaChi', models.CharField(max_length=100)),
                ('DienThoai', models.CharField(max_length=15)),
            ],
        ),
    ]
