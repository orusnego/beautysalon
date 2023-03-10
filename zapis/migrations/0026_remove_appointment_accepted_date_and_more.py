# Generated by Django 4.0 on 2023-03-02 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zapis', '0025_bookingslots'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='accepted_date',
        ),
        migrations.RemoveField(
            model_name='bookingslots',
            name='end_time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='day',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zapis.bookingdays'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='slot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zapis.bookingslots'),
        ),
    ]
