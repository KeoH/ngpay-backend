# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-19 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20170919_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='description',
        ),
    ]
