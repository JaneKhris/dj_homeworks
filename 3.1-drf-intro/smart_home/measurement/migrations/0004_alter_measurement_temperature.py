# Generated by Django 4.1.5 on 2023-01-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_rename_tempetature_measurement_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.FloatField(),
        ),
    ]