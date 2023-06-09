# Generated by Django 3.2.19 on 2023-06-09 08:55

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('custom_task', '0004_auto_20230609_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtask',
            name='due_date',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 6, 10, 8, 55, 39, 267961, tzinfo=utc), django.core.validators.MaxValueValidator(datetime.datetime(2026, 3, 5, 8, 55, 39, 267971, tzinfo=utc)))]),
        ),
        migrations.AlterField(
            model_name='customtask',
            name='start_date',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 6, 10, 8, 55, 39, 268001, tzinfo=utc), django.core.validators.MaxValueValidator(datetime.datetime(2026, 3, 5, 8, 55, 39, 268004, tzinfo=utc)))]),
        ),
    ]
