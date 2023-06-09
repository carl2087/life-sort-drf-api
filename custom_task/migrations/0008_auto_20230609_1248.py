# Generated by Django 3.2.19 on 2023-06-09 12:48

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('custom_task', '0007_auto_20230609_1128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customtask',
            options={'ordering': ['start_date']},
        ),
        migrations.AlterField(
            model_name='customtask',
            name='due_date',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 6, 10, 12, 48, 49, 117583, tzinfo=utc)), django.core.validators.MaxValueValidator(datetime.datetime(2026, 3, 5, 12, 48, 49, 117593, tzinfo=utc))]),
        ),
        migrations.AlterField(
            model_name='customtask',
            name='start_date',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 6, 10, 12, 48, 49, 117611, tzinfo=utc), django.core.validators.MaxValueValidator(datetime.datetime(2026, 3, 5, 12, 48, 49, 117614, tzinfo=utc)))]),
        ),
    ]
