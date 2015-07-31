# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('openid', models.CharField(max_length=200)),
                ('j_username', models.CharField(max_length=200)),
                ('j_password', models.CharField(max_length=200)),
            ],
        ),
    ]
