# Generated by Django 3.0.7 on 2020-07-08 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0024_auto_20200707_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='Number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='block',
            unique_together={('compound', 'Number')},
        ),
        migrations.AlterUniqueTogether(
            name='flat',
            unique_together={('Number', 'tower')},
        ),
        migrations.AlterUniqueTogether(
            name='store',
            unique_together={('tower', 'Number')},
        ),
        migrations.AlterUniqueTogether(
            name='tower',
            unique_together={('block', 'Number')},
        ),
    ]
