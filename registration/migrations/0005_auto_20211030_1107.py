# Generated by Django 3.2.7 on 2021-10-30 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20211029_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursereg',
            name='chscore',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='coursereg',
            name='handson',
            field=models.IntegerField(default=-1),
        ),
    ]
