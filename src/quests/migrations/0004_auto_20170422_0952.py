# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0003_auto_20170422_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='quest_type',
            field=models.CharField(choices=[('STORY', 'Main Story Quest'), ('SIDE', 'Side Quest'), ('SHRINE', 'Shrine Quest'), ('MEMORY', 'Memories')], default='STORY', max_length=20),
        ),
    ]