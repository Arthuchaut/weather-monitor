# Generated by Django 3.2.6 on 2021-08-26 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0010_alter_measure_wind_gust'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure',
            name='ground_level',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='measure',
            name='sea_level',
            field=models.IntegerField(null=True),
        ),
    ]
