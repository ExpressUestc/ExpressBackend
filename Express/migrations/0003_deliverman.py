# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Express', '0002_express_pos'),
    ]

    operations = [
        migrations.CreateModel(
            name='deliverman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliverPhone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Express.Express')),
            ],
        ),
    ]
