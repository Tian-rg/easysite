# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteframe', '0006_auto_20171205_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(default='authorname@example.com', max_length=254),
        ),
    ]
