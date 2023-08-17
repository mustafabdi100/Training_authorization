# Generated by Django 4.2.4 on 2023-08-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0013_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bondagreement',
            name='finance_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Processed', 'Processed'), ('Declined', 'Declined')], default='Pending', max_length=20),
        ),
    ]
