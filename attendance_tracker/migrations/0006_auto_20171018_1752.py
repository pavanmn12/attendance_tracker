# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-18 12:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tracker', '0005_auto_20171018_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='extended',
            new_name='extended1',
        ),
    ]
