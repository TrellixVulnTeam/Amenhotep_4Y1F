# Generated by Django 3.0.7 on 2020-07-08 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0026_auto_20200708_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='Number',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
