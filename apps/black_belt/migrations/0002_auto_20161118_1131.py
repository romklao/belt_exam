# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 19:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('black_belt', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wishlist',
            new_name='Item',
        ),
    ]