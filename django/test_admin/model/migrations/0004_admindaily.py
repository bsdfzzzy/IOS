# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-06 05:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_auto_20160206_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admindaily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.Admin')),
            ],
        ),
    ]
