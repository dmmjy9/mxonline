# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-21 21:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_courseorg_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseorg',
            name='tag',
        ),
    ]
