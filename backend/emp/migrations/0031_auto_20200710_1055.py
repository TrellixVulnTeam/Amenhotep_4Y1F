# Generated by Django 3.0.7 on 2020-07-10 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0030_auto_20200708_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_flat', to='emp.Owner'),
        ),
    ]
