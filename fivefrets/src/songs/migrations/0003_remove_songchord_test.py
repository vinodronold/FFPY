# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 04:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20161212_0338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songchord',
            name='test',
        ),
    ]
