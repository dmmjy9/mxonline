# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-26 21:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20171025_2311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseorg',
            old_name='catgory',
            new_name='category',
        ),
    ]
