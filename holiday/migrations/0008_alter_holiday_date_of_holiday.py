# Generated by Django 3.2.19 on 2023-06-08 14:48

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('holiday', '0007_alter_holiday_date_of_holiday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='date_of_holiday',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 6, 9, 14, 48, 34, 288047, tzinfo=utc), django.core.validators.MaxValueValidator(datetime.datetime(2026, 3, 4, 14, 48, 34, 288059, tzinfo=utc)))]),
        ),
    ]