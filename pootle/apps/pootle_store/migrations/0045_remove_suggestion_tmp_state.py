# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 05:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_store', '0044_set_new_suggestion_states'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestion',
            name='tmp_state',
        ),
    ]