# Generated by Django 3.2.6 on 2021-08-25 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_ocean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocean',
            name='ocean_id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
