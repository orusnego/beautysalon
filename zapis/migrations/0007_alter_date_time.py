# Generated by Django 4.0 on 2023-02-26 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapis', '0006_alter_date_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='time',
            field=models.CharField(choices=[('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00')], default=0, max_length=50, unique=True, verbose_name='Выберите время'),
        ),
    ]
