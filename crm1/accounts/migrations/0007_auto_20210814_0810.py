# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-14 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_representative'),
    ]

    operations = [
        migrations.CreateModel(
            name='regular_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('ownership_type', models.CharField(choices=[('Residential', 'Residential'), ('Corporate', 'Corporate')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='transfer_request',
            name='status',
        ),
        migrations.AddField(
            model_name='transfer_request',
            name='land',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.land'),
        ),
    ]