# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-21 02:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_donban'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donban',
            old_name='GiaMua',
            new_name='GiaBan',
        ),
    ]
