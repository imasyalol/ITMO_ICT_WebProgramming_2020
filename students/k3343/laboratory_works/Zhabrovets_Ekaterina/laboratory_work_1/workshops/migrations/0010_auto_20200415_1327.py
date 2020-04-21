# Generated by Django 3.0.5 on 2020-04-15 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0009_auto_20200415_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='type',
            field=models.CharField(choices=[('Оплата', 'Оплата'), ('Дресс-код', 'Дресс-код'), ('Уровень подготовки', 'Уровень подготовки'), ('Другое', 'Другое')], default='Оплата', max_length=20, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='level',
            field=models.CharField(choices=[('Начинающий', 'Начинающий'), ('Продвинутый', 'Продвинутый'), ('Любой', 'Любой')], max_length=20, verbose_name='Уроовень подготовки'),
        ),
    ]
