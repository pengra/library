# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_pollchoice_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollquestion',
            name='kiosk',
            field=models.ManyToManyField(blank=True, null=True, to='registration.Kiosk'),
        ),
    ]