# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-22 08:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': '微博', 'verbose_name_plural': '微博'},
        ),
    ]
