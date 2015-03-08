# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_remove_challenge_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='type',
            field=models.CharField(default=b'N', max_length=1, choices=[(b'V', b'D\xc3\xa9fi valid\xc3\xa9 :D'), (b'R', b'D\xc3\xa9fi rejet\xc3\xa9 :/'), (b'P', b'D\xc3\xa9fi en cours de validation ;)'), (b'N', b'D\xc3\xa9fi pas encore lu')]),
            preserve_default=True,
        ),
    ]
