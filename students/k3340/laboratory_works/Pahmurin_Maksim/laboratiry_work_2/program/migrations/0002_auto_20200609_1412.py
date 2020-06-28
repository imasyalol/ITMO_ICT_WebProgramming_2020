# Generated by Django 3.0.7 on 2020-06-09 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.Students', verbose_name='Студент'),
        ),
        migrations.AlterField(
            model_name='students',
            name='surname',
            field=models.CharField(max_length=150, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='surname',
            field=models.CharField(max_length=150, verbose_name='Фамилия'),
        ),
    ]