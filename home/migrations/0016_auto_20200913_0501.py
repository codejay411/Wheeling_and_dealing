# Generated by Django 3.1.1 on 2020-09-12 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20200913_0500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='postngo',
            name='timestamp',
        ),
    ]
