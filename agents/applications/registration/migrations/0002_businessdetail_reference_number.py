# Generated by Django 5.0.2 on 2024-02-21 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessdetail',
            name='reference_number',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
