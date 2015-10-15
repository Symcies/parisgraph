# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151015_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('prix', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vendeur',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('produits', models.ManyToManyField(to='blog.Produit', through='blog.Offre')),
            ],
        ),
        migrations.AddField(
            model_name='offre',
            name='produit',
            field=models.ForeignKey(to='blog.Produit'),
        ),
        migrations.AddField(
            model_name='offre',
            name='vendeur',
            field=models.ForeignKey(to='blog.Vendeur'),
        ),
    ]
