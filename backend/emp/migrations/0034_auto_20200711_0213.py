# Generated by Django 3.0.7 on 2020-07-11 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0033_auto_20200710_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='id',
        ),
        migrations.AlterField(
            model_name='admin',
            name='Username',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='Avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
