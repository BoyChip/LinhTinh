# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-13 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_khachhang'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hang',
            fields=[
                ('MaHang', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('TenHang', models.CharField(max_length=50, unique=True)),
                ('SoLuong', models.IntegerField()),
                ('GiaMuaVao', models.DecimalField(decimal_places=2, max_digits=15)),
                ('GiaBanRa', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
    ]
