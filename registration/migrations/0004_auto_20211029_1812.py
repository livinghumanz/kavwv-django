# Generated by Django 3.2.7 on 2021-10-29 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20211029_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursereg',
            name='chscore',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coursereg',
            name='handson',
            field=models.IntegerField(default=0),
        ),
    ]
