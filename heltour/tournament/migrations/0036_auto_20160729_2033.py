# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0035_auto_20160728_2157'),
    ]

    operations = [
        migrations.RunSQL('''UPDATE tournament_playerpairing SET game_link='' WHERE game_link IS NULL'''),
        migrations.RunSQL('''UPDATE tournament_playerpairing SET result='' WHERE result IS NULL'''),
    ]