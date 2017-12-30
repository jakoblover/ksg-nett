# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-17 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedules.Schedule')),
            ],
        ),
        migrations.CreateModel(
            name='ShiftSlotDayRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule', models.CharField(choices=[('mo', 'Monday'), ('tu', 'Tuesday'), ('we', 'Wednesday'), ('th', 'Thursday'), ('fr', 'Friday'), ('sa', 'Saturday'), ('su', 'Sunday'), ('wk', 'Weekdays'), ('ed', 'Weekends'), ('fu', 'Full weekends')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ShiftSlotGroupTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('schedule_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedules.ScheduleTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='ShiftSlotTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedules.ShiftSlotGroupTemplate')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedules.ScheduleSlotType')),
            ],
        ),
        migrations.AddField(
            model_name='shiftslotdayrule',
            name='shift_slot_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day_rules', to='schedules.ShiftSlotGroupTemplate'),
        ),
    ]
