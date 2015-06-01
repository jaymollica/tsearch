# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_artwork_valid_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='valid_url',
        ),
    ]
