# Generated by Django 3.2.19 on 2023-06-07 12:59

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('holiday', '0003_alter_holiday_date_of_holiday'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='holiday',
            options={'ordering': ['date_of_holiday']},
        ),
        migrations.AlterField(
            model_name='holiday',
            name='date_of_holiday',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 6, 8, 12, 59, 6, 985840, tzinfo=utc), django.core.validators.MaxValueValidator(datetime.datetime(2026, 3, 3, 12, 59, 6, 985855, tzinfo=utc)))]),
        ),
    ]
