# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20160726_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(default='(No Subject)', max_length=256),
        ),
    ]
