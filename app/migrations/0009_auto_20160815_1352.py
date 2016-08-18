# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 13:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0008_auto_20160815_1258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('created', 'num_views')},
        ),
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': ('created', 'num_views', 'num_votes')},
        ),
        migrations.RemoveField(
            model_name='event',
            name='num_votes',
        ),
        migrations.AddField(
            model_name='answer',
            name='for_question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='answers_voted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='questions_voted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='story',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='stories_voted', to=settings.AUTH_USER_MODEL),
        ),
    ]
