# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 05:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('househunt', '0002_auto_20170522_0147'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='House',
            new_name='Property',
        ),
    ]