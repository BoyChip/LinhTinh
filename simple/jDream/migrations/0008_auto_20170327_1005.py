# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jDream', '0007_auto_20170327_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chitiethdban',
            name='MaHang',
        ),
        migrations.AddField(
            model_name='chitiethdban',
            name='MaHang',
            field=models.ManyToManyField(to='jDream.Hang'),
        ),
    ]
