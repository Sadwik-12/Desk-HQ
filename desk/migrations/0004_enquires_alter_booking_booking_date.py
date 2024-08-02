# Generated by Django 4.1.7 on 2023-03-30 12:12

import datetime
import desk.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0003_alter_booking_booking_date_alter_booking_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=80)),
                ('message', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 31, 12, 12, 46, 488875), validators=[desk.models.validate_date]),
        ),
    ]