# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 00:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0001_initial'),
        ('api', '0002_auto_20171106_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='apicall',
            name='merchant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_calls', to='merchants.Merchant'),
        ),
    ]
