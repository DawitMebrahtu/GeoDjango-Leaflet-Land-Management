# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-10 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_ownershipform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_coordinate', models.IntegerField(null=True)),
                ('y_coordinate', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='owner',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='owner',
            name='ownership',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]