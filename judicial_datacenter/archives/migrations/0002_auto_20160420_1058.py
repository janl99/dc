# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sfxzjgjbxx',
            name='JGLB',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archives.JGLB'),
        ),
        migrations.AlterField(
            model_name='sfxzjgjbxx',
            name='JGLSCJ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archives.JGLSCJ'),
        ),
        migrations.AlterField(
            model_name='sfxzjgjbxx',
            name='JGXZJB',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archives.JGXZJB'),
        ),
    ]
