# Generated by Django 3.2.6 on 2021-08-24 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_alter_transfer_request_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='phone',
        ),
    ]
