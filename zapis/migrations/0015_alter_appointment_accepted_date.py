# Generated by Django 4.0 on 2023-03-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapis', '0014_alter_appointment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='accepted_date',
            field=models.DateTimeField(),
        ),
    ]
