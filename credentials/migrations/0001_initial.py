# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 23:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Ultima modificación')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('credential_type', models.CharField(choices=[('Real', 'real'), ('Sandbox', 'sandbox')], default='sandbox', max_length=10)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credentials', to='accounts.Account')),
            ],
            options={
                'ordering': ['-creation_date'],
                'abstract': False,
            },
        ),
    ]
