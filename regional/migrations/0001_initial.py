# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comuna', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Comunas',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_provincia', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Provincias',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_region', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Regiones',
            },
        ),
        migrations.AddField(
            model_name='provincia',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regional.Region'),
        ),
        migrations.AddField(
            model_name='comuna',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regional.Provincia'),
        ),
    ]
