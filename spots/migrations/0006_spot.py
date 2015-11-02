# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0005_delete_spot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('idn', models.IntegerField(unique=True)),
                ('s_name', models.CharField(max_length=200)),
                ('s_description', models.CharField(max_length=1000)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('tourist_weight', models.IntegerField()),
                ('urbex_weight', models.IntegerField()),
                ('walk_weight', models.IntegerField()),
            ],
            options={
                'ordering': ('idn',),
            },
        ),
    ]
