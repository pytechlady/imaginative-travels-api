# Generated by Django 4.0.3 on 2022-04-17 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='destination_image',
            field=models.CharField(max_length=255),
        ),
    ]
