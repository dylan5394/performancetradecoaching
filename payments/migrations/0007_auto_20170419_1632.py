# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_auto_20170419_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='code_expires',
            field=models.DateTimeField(),
        ),
    ]
