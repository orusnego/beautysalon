# Generated by Django 4.0 on 2023-03-02 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zapis', '0026_remove_appointment_accepted_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingtime',
            name='end_time',
        ),
        migrations.AlterField(
            model_name='bookingtime',
            name='start_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zapis.bookingslots'),
        ),
    ]
