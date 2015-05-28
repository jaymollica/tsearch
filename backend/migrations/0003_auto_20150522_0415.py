# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_artwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='hex_str',
            field=models.CharField(max_length=6),
        ),
    ]
