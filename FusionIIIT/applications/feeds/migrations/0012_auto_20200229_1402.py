# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-29 14:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0011_auto_20200229_1159'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tags',
            unique_together=set([('user', 'my_subtag')]),
        ),
    ]
