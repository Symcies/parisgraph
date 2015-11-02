# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('idn', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('tourist_weigth', models.IntegerField()),
                ('urbex_weigth', models.IntegerField()),
                ('walk_weight', models.IntegerField()),
            ],
            options={
                'ordering': ('idn',),
            },
        ),
    ]
