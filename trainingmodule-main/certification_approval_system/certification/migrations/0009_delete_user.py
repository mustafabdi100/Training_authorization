# Generated by Django 4.2.4 on 2023-08-13 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0008_alter_user_groups'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]