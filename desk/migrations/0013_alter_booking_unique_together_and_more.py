# Generated by Django 4.1.7 on 2023-04-12 15:00

import datetime
import desk.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0012_alter_booking_booking_date'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=datetime.date(2023, 4, 13), validators=[desk.models.validate_date]),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('location', 'space_booking', 'booking_date', 'booking_start', 'booking_end')},
        ),
    ]
