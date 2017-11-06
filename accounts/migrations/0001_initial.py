# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 23:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('merchants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractAccount',
            fields=[
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Ultima modificación')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-creation_date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('abstractaccount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.AbstractAccount')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='merchants.Merchant')),
            ],
            options={
                'ordering': ['-creation_date'],
                'abstract': False,
            },
            bases=('accounts.abstractaccount',),
        ),
    ]
