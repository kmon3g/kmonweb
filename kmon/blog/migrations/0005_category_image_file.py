# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170216_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Image_File',
            field=models.ImageField(null=True, upload_to='kmon/uploaded/image/category'),
        ),
    ]
