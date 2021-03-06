# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 22:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chords', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.PositiveSmallIntegerField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube', models.SlugField(max_length=100)),
                ('name', models.CharField(default='PROCESSING . . .', max_length=100)),
                ('bpm', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('process_status', models.PositiveSmallIntegerField(choices=[(0, 'SUCCESS'), (1, 'NOT STARTED'), (2, 'PROCESSING'), (3, 'MORE THAN SETUP DURATION'), (4, 'YOUTUBE ID DOWNLOAD ERROR'), (5, 'BEAT PROCESS ERROR'), (6, 'Invalid Youtube ID')], default=1)),
                ('lyric', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='songs.Album')),
                ('composer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='songs.Composer')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('singers', models.ManyToManyField(blank=True, to='songs.Singer')),
            ],
        ),
        migrations.CreateModel(
            name='SongChord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beat_position', models.FloatField(default=-1)),
                ('start_time', models.FloatField(default=-1)),
                ('chord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chords.Chord')),
                ('modified_chord', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_chord', to='chords.Chord')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Song')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
