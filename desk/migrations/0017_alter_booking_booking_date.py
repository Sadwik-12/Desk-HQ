# Generated by Django 4.1.7 on 2024-07-21 15:27

import datetime
import desk.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0016_alter_booking_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=datetime.date(2024, 7, 22), validators=[desk.models.validate_date]),
        ),
    ]
