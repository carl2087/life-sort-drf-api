# Generated by Django 3.2.19 on 2023-06-07 12:57

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('holiday', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='date_of_holiday',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 6, 8, 12, 57, 32, 779780, tzinfo=utc), django.core.validators.MaxValueValidator(datetime.datetime(2026, 3, 3, 12, 57, 32, 779793, tzinfo=utc)))]),
        ),
    ]
