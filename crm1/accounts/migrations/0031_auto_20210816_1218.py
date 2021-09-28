# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-16 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_auto_20210816_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='land',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.land'),
        ),
        migrations.AlterField(
            model_name='transfer_request',
            name='land',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.land'),
        ),
    ]
