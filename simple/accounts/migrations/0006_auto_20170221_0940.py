# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-21 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170221_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donban',
            name='SoLuong',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='donmua',
            name='SoLuong',
            field=models.IntegerField(default=1),
        ),
    ]
