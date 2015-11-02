# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0002_auto_20151031_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spot',
            old_name='name',
            new_name='s_name',
        ),
    ]
