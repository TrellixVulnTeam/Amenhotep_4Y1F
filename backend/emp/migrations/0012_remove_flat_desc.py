# Generated by Django 3.0.7 on 2020-07-05 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0011_flat_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='Desc',
        ),
    ]
