# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songs',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='songs',
            name='track_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
    ]
