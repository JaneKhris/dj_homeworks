# Generated by Django 4.1.5 on 2023-01-28 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='tempetature',
            new_name='temperature',
        ),
    ]
