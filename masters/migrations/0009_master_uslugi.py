# Generated by Django 4.0 on 2023-02-26 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0008_alter_master_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='uslugi',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
