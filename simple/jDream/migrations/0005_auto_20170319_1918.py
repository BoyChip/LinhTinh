# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-19 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jDream', '0004_auto_20170319_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hdban',
            name='NgayBan',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
