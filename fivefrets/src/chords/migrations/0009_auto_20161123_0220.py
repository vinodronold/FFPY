# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chords', '0008_auto_20161026_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chord',
            name='name',
            field=models.CharField(choices=[('1', 'A'), ('2', 'A#'), ('3', 'B'), ('4', 'C'), ('5', 'C#'), ('6', 'D'), ('7', 'D#'), ('8', 'E'), ('9', 'F'), ('10', 'F#'), ('11', 'G'), ('12', 'G#'), ('N', 'X')], max_length=2),
        ),
    ]
