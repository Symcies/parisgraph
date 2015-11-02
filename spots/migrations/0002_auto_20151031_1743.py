# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spot',
            old_name='tourist_weigth',
            new_name='tourist_weight',
        ),
        migrations.RenameField(
            model_name='spot',
            old_name='urbex_weigth',
            new_name='urbex_weight',
        ),
    ]
