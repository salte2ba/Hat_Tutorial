# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('skills', models.CharField(max_length=1, choices=[(b'1', b'No Skill'), (b'2', b'Below Average'), (b'3', b'Average'), (b'4', b'Above Average'), (b'5', b'Pro')])),
                ('wants_shirt', models.BooleanField(default=False)),
                ('wants_frisbee', models.BooleanField(default=False)),
                ('shirtsize', models.CharField(default=b'L', max_length=1, choices=[(b'S', b'S'), (b'M', b'M'), (b'L', b'L')])),
                ('position', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'In Cutter'), (b'2', b'Out Cutter'), (b'3', b'Short Distance Handler'), (b'4', b'Long Distance Handler')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
