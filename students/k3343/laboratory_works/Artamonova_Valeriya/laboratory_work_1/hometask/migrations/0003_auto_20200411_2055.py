# Generated by Django 3.0.5 on 2020-04-11 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hometask', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hometask.UserProfile'),
        ),
    ]
