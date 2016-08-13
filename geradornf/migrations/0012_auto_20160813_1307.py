# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-13 16:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geradornf', '0011_auto_20160811_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destinatario',
            old_name='cliente_id',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='emitente',
            old_name='cliente_id',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='cliente_id',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='transportador',
            old_name='cliente_id',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='transportadorcontrato',
            old_name='transportador_id',
            new_name='transportador',
        ),
    ]