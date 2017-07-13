# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 18:03
from __future__ import unicode_literals

import hashlib
import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    atomic = False
    dependencies = [
        ('alerts', '0005_populate_muzzle_hashes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='muzzle_hash',
            field=models.CharField(
                blank=True,
                db_index=True,
                max_length=64,
                null=True,
                unique=True,
            ),
        ),
    ]
