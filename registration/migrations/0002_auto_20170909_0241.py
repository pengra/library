# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-09 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='school',
            name='contact_email',
        ),
        migrations.AddField(
            model_name='teacher',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.School'),
        ),
        migrations.AddField(
            model_name='school',
            name='primary_contact',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_contact_for', to='registration.Teacher'),
        ),
    ]
