# Generated by Django 3.0.5 on 2020-05-28 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newproj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoholder',
            name='holders',
            field=models.ManyToManyField(through='newproj.Holding', to='newproj.Automobile'),
        ),
    ]
