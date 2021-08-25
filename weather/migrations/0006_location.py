# Generated by Django 3.2.6 on 2021-08-25 07:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_alter_ocean_ocean_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('lat', models.FloatField(validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('lon', models.FloatField(validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.city')),
                ('ocean', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.ocean')),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
                'db_table': 'location',
            },
        ),
    ]