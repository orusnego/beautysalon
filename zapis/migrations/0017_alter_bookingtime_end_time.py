# Generated by Django 4.0 on 2023-03-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapis', '0016_alter_bookingtime_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingtime',
            name='end_time',
            field=models.TimeField(),
        ),
    ]
