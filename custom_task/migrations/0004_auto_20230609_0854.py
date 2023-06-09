# Generated by Django 3.2.19 on 2023-06-09 08:54

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('custom_task', '0003_auto_20230608_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtask',
            name='due_date',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 6, 10, 8, 54, 48, 663099, tzinfo=utc), django.core.validators.MaxValueValidator(datetime.datetime(2026, 3, 5, 8, 54, 48, 663108, tzinfo=utc)))]),
        ),
        migrations.AlterField(
            model_name='customtask',
            name='start_date',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 6, 10, 8, 54, 48, 663146, tzinfo=utc), django.core.validators.MaxValueValidator(datetime.datetime(2026, 3, 5, 8, 54, 48, 663149, tzinfo=utc)))]),
        ),
    ]
