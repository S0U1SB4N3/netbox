# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 14:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circuits', '0003_auto_20160621_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='circuit',
            name='created',
            field=models.DateField(auto_now_add=True, default=datetime.date(2016, 6, 22)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='circuit',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 22, 14, 10, 28, 340517)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider',
            name='created',
            field=models.DateField(auto_now_add=True, default=datetime.date(2016, 6, 22)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 22, 14, 10, 40, 964944)),
            preserve_default=False,
        ),
    ]
