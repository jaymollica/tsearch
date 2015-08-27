# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('artist', models.CharField(default=b'', max_length=100)),
                ('color', models.ForeignKey(to='backend.Color')),
                ('country', models.ForeignKey(to='backend.Country')),
                ('medium', models.ForeignKey(to='backend.Medium')),
            ],
        ),
    ]
