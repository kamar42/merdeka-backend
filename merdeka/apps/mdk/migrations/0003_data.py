# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdk', '0002_auto_20150822_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=19, decimal_places=2)),
                ('city', models.ForeignKey(to='mdk.City')),
                ('commodity', models.ForeignKey(to='mdk.Commodities')),
                ('goods', models.ForeignKey(to='mdk.Goods')),
                ('goods_child', models.ForeignKey(to='mdk.GoodsChilds')),
                ('province', models.ForeignKey(to='mdk.Province')),
                ('unit', models.ForeignKey(to='mdk.BaseUnit')),
                ('venue', models.ForeignKey(to='mdk.Venues')),
            ],
            options={
                'db_table': 'master_data',
                'verbose_name': 'Data',
                'verbose_name_plural': 'Data',
            },
        ),
    ]
