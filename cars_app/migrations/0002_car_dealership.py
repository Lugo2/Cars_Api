# Generated by Django 4.1 on 2022-08-27 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealerships', '0001_initial'),
        ('cars_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='dealership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dealerships.dealership'),
        ),
    ]
