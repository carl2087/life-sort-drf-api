# Generated by Django 3.2.19 on 2023-06-09 14:48

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quick_task', '0009_alter_quicktask_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quicktask',
            name='due_date',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 6, 10, 14, 48, 48, 423906, tzinfo=utc)), django.core.validators.MaxValueValidator(datetime.datetime(2026, 3, 5, 14, 48, 48, 423918, tzinfo=utc))]),
        ),
    ]