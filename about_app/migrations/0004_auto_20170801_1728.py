# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0003_auto_20170801_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=48, verbose_name='Название'),
        ),
    ]
