# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-18 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tracker', '0002_auto_20171018_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='worked_for',
            field=models.TimeField(blank=True, null=True),
        ),
    ]