# Generated by Django 4.1.7 on 2023-03-30 14:30

import datetime
import desk.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0004_enquires_alter_booking_booking_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Enquires',
            new_name='Enquiry',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 31, 14, 30, 17, 586192), validators=[desk.models.validate_date]),
        ),
    ]
