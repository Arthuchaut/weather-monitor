# Generated by Django 3.2.6 on 2021-08-24 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'country', 'verbose_name_plural': 'countries'},
        ),
        migrations.AlterModelTable(
            name='country',
            table='country',
        ),
    ]