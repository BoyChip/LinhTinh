# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-21 07:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20170221_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donban',
            name='id',
        ),
        migrations.RemoveField(
            model_name='donmua',
            name='id',
        ),
        migrations.AlterField(
            model_name='donban',
            name='MaHang',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.MatHang'),
        ),
        migrations.AlterField(
            model_name='donmua',
            name='MaHang',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.MatHang'),
        ),
    ]
