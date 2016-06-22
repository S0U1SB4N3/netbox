# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 14:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0005_delete_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='aggregate',
            name='created',
            field=models.DateField(auto_now_add=True, default=datetime.date(2016, 6, 22)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aggregate',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 22, 14, 12, 29, 891569)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='created',
            field=models.DateField(auto_now_add=True, default=datetime.date(2016, 6, 22)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 22, 14, 12, 39, 666885)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prefix',
            name='created',
            field=models.DateField(auto_now_add=True, default=datetime.date(2016, 6, 22)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prefix',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 22, 14, 12, 48, 11411)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vlan',
            name='created',
            field=models.DateField(auto_now_add=True, default=datetime.date(2016, 6, 22)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vlan',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 22, 14, 12, 56, 963230)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vrf',
            name='created',
            field=models.DateField(auto_now_add=True, default=datetime.date(2016, 6, 22)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vrf',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 22, 14, 13, 4, 387113)),
            preserve_default=False,
        ),
    ]
