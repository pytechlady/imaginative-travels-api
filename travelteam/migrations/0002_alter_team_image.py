# Generated by Django 4.0.10 on 2023-07-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelteam', '0001_AddedTeamView'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.URLField(),
        ),
    ]
