# Generated by Django 3.0.7 on 2020-07-05 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0014_block_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='Papers',
        ),
    ]
