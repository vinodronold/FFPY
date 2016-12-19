# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_remove_songchord_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='process_status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'SUCCESS'), (1, 'NOT STARTED'), (2, 'PROCESSING'), (3, 'MORE THAN SETUP DURATION'), (4, 'YOUTUBE ID DOWNLOAD ERROR'), (5, 'BEAT PROCESS ERROR'), (6, 'Invalid Youtube ID')], default=1),
        ),
    ]