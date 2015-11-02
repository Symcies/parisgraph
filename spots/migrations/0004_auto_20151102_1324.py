# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0003_auto_20151102_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spot',
            old_name='description',
            new_name='s_description',
        ),
    ]
