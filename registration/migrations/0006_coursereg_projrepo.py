# Generated by Django 3.2.7 on 2021-11-01 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20211030_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursereg',
            name='projrepo',
            field=models.TextField(null=True),
        ),
    ]
