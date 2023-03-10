# Generated by Django 4.0 on 2023-02-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0003_review_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='works/images')),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(default='Аноним', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(max_length=10000),
        ),
    ]
