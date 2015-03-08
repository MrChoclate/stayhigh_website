# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, verbose_name=b'Pr\xc3\xa9nom', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name=b'Nom', blank=True)),
                ('type', models.CharField(default=b'N', max_length=1, choices=[(b'V', b'D\xc3\xa9fi valid\xc3\xa9 :D'), (b'R', b'D\xc3\xa9fi rejet\xc3\xa9 :/'), (b'P', b'D\xc3\xa9fi en cours de validation ;)'), (b'N', b'D\xc3\xa9fi pas encore lu')])),
                ('content', models.TextField(verbose_name=b'Le D\xc3\xa9fi')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
