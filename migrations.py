# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20150218_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='track_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='track_name',
        ),
    ]
