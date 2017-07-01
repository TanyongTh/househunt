# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-24 21:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('househunt', '0009_auto_20170624_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='createdate',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='listedagent',
            new_name='listed_agent',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='listeddate',
            new_name='listed_date',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='modifydate',
            new_name='modify_date',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='propertyid',
            new_name='property_id',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='solddate',
            new_name='sold_date',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='soldprice',
            new_name='sold_price',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='suburbname',
            new_name='suburb_name',
        ),
    ]
