# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20171116_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ksg_status',
            field=models.CharField(choices=[('aktiv', 'Aktiv'), ('inaktiv', 'Ikke aktiv'), ('permittert', 'Permittert'), ('sluttet', 'Sluttet før tiden')], default=('aktiv', 'Aktiv'), max_length=32),
        ),
    ]
