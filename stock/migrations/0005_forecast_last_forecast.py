# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_forecast'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecast',
            name='last_forecast',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
