# Generated by Django 4.2.4 on 2023-08-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeerequest',
            name='feedback',
            field=models.TextField(blank=True),
        ),
    ]
