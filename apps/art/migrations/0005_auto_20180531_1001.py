# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-31 10:01
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0004_auto_20180530_1130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='art',
            options={'ordering': ['a_addtime'], 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['t_createtime'], 'verbose_name_plural': '标签'},
        ),
        migrations.AlterField(
            model_name='art',
            name='a_addtime',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='art',
            name='a_content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='文章内容'),
        ),
        migrations.AlterField(
            model_name='art',
            name='a_updatetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更改时间'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='t_createtime',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
    ]
