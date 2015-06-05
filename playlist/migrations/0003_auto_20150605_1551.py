# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0002_auto_20150605_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='order',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='song',
            name='source',
            field=models.CharField(max_length=10, choices=[(b'youtube', b'youtube'), (b'soundcloud', b'SoundCloud')]),
        ),
    ]
