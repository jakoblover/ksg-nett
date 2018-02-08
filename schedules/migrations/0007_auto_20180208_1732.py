# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-08 17:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedules', '0006_shiftslotgroupinterest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'verbose_name_plural': 'schedules'},
        ),
        migrations.AlterModelOptions(
            name='scheduleslottype',
            options={'verbose_name_plural': 'schedule slot types'},
        ),
        migrations.AlterModelOptions(
            name='scheduletemplate',
            options={'verbose_name_plural': 'schedule templates'},
        ),
        migrations.AlterModelOptions(
            name='shift',
            options={'verbose_name_plural': 'shifts'},
        ),
        migrations.AlterModelOptions(
            name='shiftslot',
            options={'verbose_name_plural': 'Shift slots'},
        ),
        migrations.AlterModelOptions(
            name='shiftslotdayrule',
            options={'verbose_name_plural': 'Shift slot day rules'},
        ),
        migrations.AlterModelOptions(
            name='shiftslotgroup',
            options={'verbose_name_plural': 'shift slot groups'},
        ),
        migrations.AlterModelOptions(
            name='shiftslotgroupinterest',
            options={'verbose_name_plural': 'Shift slot group interest'},
        ),
        migrations.AlterModelOptions(
            name='shiftslotgrouptemplate',
            options={'verbose_name_plural': 'shift slot group templates'},
        ),
        migrations.AlterModelOptions(
            name='shiftslottemplate',
            options={'verbose_name_plural': 'Shift slot templates'},
        ),
        migrations.AlterModelOptions(
            name='shifttrade',
            options={'verbose_name_plural': 'Shift trade'},
        ),
        migrations.AlterModelOptions(
            name='shifttradeoffer',
            options={'verbose_name_plural': 'Shift trade offer'},
        ),
        migrations.AlterUniqueTogether(
            name='scheduleslottype',
            unique_together=set([('name', 'schedule')]),
        ),
        migrations.AlterUniqueTogether(
            name='scheduletemplate',
            unique_together=set([('name', 'schedule')]),
        ),
        migrations.AlterUniqueTogether(
            name='shiftslotdayrule',
            unique_together=set([('rule', 'shift_slot_template')]),
        ),
        migrations.AlterUniqueTogether(
            name='shiftslotgroup',
            unique_together=set([('name', 'schedule')]),
        ),
        migrations.AlterUniqueTogether(
            name='shiftslotgroupinterest',
            unique_together=set([('shift_group', 'user')]),
        ),
    ]