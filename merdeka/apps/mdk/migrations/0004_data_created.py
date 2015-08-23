# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mdk', '0003_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
