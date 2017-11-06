# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APICalls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Ultima modificación')),
                ('method', models.CharField(choices=[('get', 'GET'), ('post', 'POST'), ('delete', 'DELETE'), ('put', 'PUT'), ('patch', 'PATCH')], default='POST', max_length=6)),
            ],
            options={
                'ordering': ['-creation_date'],
                'abstract': False,
            },
        ),
    ]