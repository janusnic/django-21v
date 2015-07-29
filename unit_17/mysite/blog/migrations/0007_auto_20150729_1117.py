# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150727_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categoty',
            new_name='category',
        ),
    ]
