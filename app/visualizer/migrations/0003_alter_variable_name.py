# Generated by Django 5.1.5 on 2025-01-21 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0002_alter_currency_options_variable_external_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variable',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
