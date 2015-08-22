# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('unique_name', models.SlugField(unique=True, max_length=200, editable=False, blank=True)),
                ('condition', models.CharField(max_length=120, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(editable=False, blank=True)),
            ],
            options={
                'db_table': 'master_base_unit',
                'verbose_name': 'Base Unit',
                'verbose_name_plural': 'Base Unit',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('unique_name', models.SlugField(unique=True, max_length=200, editable=False, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(editable=False, blank=True)),
            ],
            options={
                'db_table': 'master_City',
                'verbose_name': 'City',
                'verbose_name_plural': 'City',
            },
        ),
        migrations.CreateModel(
            name='Commodities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('unique_name', models.SlugField(unique=True, max_length=200, editable=False, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(editable=False, blank=True)),
            ],
            options={
                'db_table': 'master_commodities',
                'verbose_name': 'Commodities',
                'verbose_name_plural': 'Commodities',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('unique_name', models.SlugField(unique=True, max_length=200, editable=False, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(editable=False, blank=True)),
                ('commodity', models.ForeignKey(to='mdk.Commodities')),
            ],
            options={
                'db_table': 'master_goods',
                'verbose_name': 'Goods',
                'verbose_name_plural': 'Goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsChilds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('unique_name', models.SlugField(unique=True, max_length=200, editable=False, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(editable=False, blank=True)),
                ('goods', models.ForeignKey(to='mdk.Goods')),
            ],
            options={
                'db_table': 'master_goods_childs',
                'verbose_name': 'Goods Childs',
                'verbose_name_plural': 'Goods Childs',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('unique_name', models.SlugField(unique=True, max_length=200, editable=False, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(editable=False, blank=True)),
            ],
            options={
                'db_table': 'master_province',
                'verbose_name': 'Province',
                'verbose_name_plural': 'Province',
            },
        ),
        migrations.CreateModel(
            name='TypeVenue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('unique_name', models.SlugField(unique=True, max_length=200, editable=False, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(editable=False, blank=True)),
            ],
            options={
                'db_table': 'master_type_venue',
                'verbose_name': 'Type Venue',
                'verbose_name_plural': 'Type Venue',
            },
        ),
        migrations.CreateModel(
            name='Venues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('unique_name', models.SlugField(unique=True, max_length=200, editable=False, blank=True)),
                ('address', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(editable=False, blank=True)),
                ('city', models.ForeignKey(to='mdk.City')),
                ('type_venue', models.ForeignKey(to='mdk.TypeVenue')),
            ],
            options={
                'db_table': 'master_venues',
                'verbose_name': 'Venues',
                'verbose_name_plural': 'Venues',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(to='mdk.Province'),
        ),
    ]
