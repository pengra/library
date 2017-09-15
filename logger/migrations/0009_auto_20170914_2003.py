# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0008_auto_20170914_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(blank=True, choices=[('09', 'Freshman'), ('10', 'Sophomore'), ('11', 'Junior'), ('12', 'Senior'), ('GD', 'Graduated')], max_length=2),
        ),
    ]