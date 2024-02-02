# Generated by Django 5.0.1 on 2024-02-01 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('year', models.PositiveIntegerField()),
                ('mileage', models.IntegerField()),
                ('description', models.TextField()),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='photos')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.vehicle')),
            ],
        ),
    ]