# Generated by Django 4.0 on 2023-02-18 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='image',
            field=models.ImageField(upload_to='masters/images'),
        ),
    ]
