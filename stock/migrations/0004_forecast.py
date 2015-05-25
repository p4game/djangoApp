# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20150524_0845'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForeCast',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('value', models.IntegerField()),
                ('user', models.ForeignKey(to='stock.User')),
            ],
        ),
    ]
