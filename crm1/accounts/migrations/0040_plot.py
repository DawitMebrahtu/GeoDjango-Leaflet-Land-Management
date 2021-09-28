# Generated by Django 3.2.6 on 2021-08-23 16:51

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0039_land_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='plot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('zip_code', models.CharField(max_length=5, null=True)),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
            ],
        ),
    ]
