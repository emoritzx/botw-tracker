# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questentry',
            name='completion_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='questentry',
            name='discovery_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
