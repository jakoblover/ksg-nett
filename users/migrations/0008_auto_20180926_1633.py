# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-26 16:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180926_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergy',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='allergies', to=settings.AUTH_USER_MODEL),
        ),
    ]