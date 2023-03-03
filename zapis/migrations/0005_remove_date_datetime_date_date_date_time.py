# Generated by Django 4.0 on 2023-02-26 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapis', '0004_date_delete_zapis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='datetime',
        ),
        migrations.AddField(
            model_name='date',
            name='date',
            field=models.DateField(default='1999-01-01'),
        ),
        migrations.AddField(
            model_name='date',
            name='time',
            field=models.CharField(choices=[('8:00', '8:00'), ('9:00', '9:00'), ('9:00', '9:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00')], default=0, max_length=50, unique=True, verbose_name='Выберите время'),
        ),
    ]
