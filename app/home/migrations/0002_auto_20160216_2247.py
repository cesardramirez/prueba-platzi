# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionuserdata',
            name='amount',
            field=models.IntegerField(verbose_name='Monto o cantidad'),
        ),
    ]
