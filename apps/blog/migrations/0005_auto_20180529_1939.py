# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-29 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180529_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='user',
            field=models.IntegerField(blank=True, null=True, verbose_name='用户'),
        ),
    ]
