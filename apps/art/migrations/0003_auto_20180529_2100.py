# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-29 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0002_auto_20180529_1752'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'tag'},
        ),
        migrations.AlterField(
            model_name='art',
            name='a_img',
            field=models.ImageField(blank=True, null=True, upload_to='apps/static/uploads'),
        ),
    ]
