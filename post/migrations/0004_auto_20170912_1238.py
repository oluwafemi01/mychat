# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 19:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20170430_2251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='firstname',
            new_name='channelname',
        ),
        migrations.RemoveField(
            model_name='post',
            name='email',
        ),
        migrations.RemoveField(
            model_name='post',
            name='lastname',
        ),
    ]