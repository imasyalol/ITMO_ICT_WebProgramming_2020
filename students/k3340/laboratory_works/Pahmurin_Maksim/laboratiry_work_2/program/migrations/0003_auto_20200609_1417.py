# Generated by Django 3.0.7 on 2020-06-09 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_auto_20200609_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='group_number',
            field=models.CharField(max_length=10, verbose_name='Номер группы'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='class_number',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Номер кабинета'),
        ),
    ]