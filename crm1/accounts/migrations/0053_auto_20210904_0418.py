# Generated by Django 3.2.6 on 2021-09-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0052_auto_20210902_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='ownership_type',
        ),
        migrations.AddField(
            model_name='poly',
            name='ownership_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='poly',
            name='visibility',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
