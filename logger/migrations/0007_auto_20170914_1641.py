# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 23:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0006_kiosksession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kiosksession',
            name='hours',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='kiosksession',
            name='minutes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='kiosksession',
            name='signout',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='session_signout', to='logger.Log'),
        ),
    ]
