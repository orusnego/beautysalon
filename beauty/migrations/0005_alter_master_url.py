# Generated by Django 4.0 on 2023-02-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0004_master_description_master_url_alter_master_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
