# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 09:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0003_auto_20160420_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='jglb',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='archives.JGLB'),
        ),
    ]
