# Generated by Django 3.0.7 on 2020-07-07 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0023_auto_20200706_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='Type',
            field=models.CharField(choices=[('request', 'request'), ('complaint', 'complaint')], default='request', max_length=9),
        ),
    ]
