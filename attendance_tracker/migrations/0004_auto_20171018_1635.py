# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-18 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tracker', '0003_attendance_worked_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='worked_for',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
