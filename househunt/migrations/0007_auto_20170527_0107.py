# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('househunt', '0006_auto_20170526_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='ListedDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='SoldDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]