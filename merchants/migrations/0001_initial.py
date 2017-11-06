# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 23:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Ultima modificación')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('fiscal_code', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-creation_date'],
                'abstract': False,
            },
        ),
    ]
