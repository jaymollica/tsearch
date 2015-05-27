# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20150522_0415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='color',
        ),
        migrations.AddField(
            model_name='artwork',
            name='date_created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='svg',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='medium',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
