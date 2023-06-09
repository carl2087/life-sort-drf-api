# Generated by Django 3.2.19 on 2023-06-09 14:48

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('custom_task', '0008_auto_20230609_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtask',
            name='due_date',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 6, 10, 14, 48, 48, 424696, tzinfo=utc)), django.core.validators.MaxValueValidator(datetime.datetime(2026, 3, 5, 14, 48, 48, 424707, tzinfo=utc))]),
        ),
        migrations.AlterField(
            model_name='customtask',
            name='start_date',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 6, 10, 14, 48, 48, 424725, tzinfo=utc)), django.core.validators.MaxValueValidator(datetime.datetime(2026, 3, 5, 14, 48, 48, 424730, tzinfo=utc))]),
        ),
    ]
