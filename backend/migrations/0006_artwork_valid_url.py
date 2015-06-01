# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20150527_0551'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='valid_url',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
