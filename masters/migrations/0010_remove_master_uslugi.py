# Generated by Django 4.0 on 2023-02-26 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0009_master_uslugi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='uslugi',
        ),
    ]
