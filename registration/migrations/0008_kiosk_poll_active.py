# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_kiosk_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='kiosk',
            name='poll_active',
            field=models.BooleanField(default=True),
        ),
    ]