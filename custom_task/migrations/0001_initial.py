# Generated by Django 3.2.19 on 2023-06-08 12:55

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('due_date', models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 6, 9, 12, 55, 18, 932861, tzinfo=utc), django.core.validators.MaxValueValidator(datetime.datetime(2026, 3, 4, 12, 55, 18, 932868, tzinfo=utc)))])),
                ('start_date', models.DateTimeField(blank=True, validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 6, 9, 12, 55, 18, 932892, tzinfo=utc), django.core.validators.MaxValueValidator(datetime.datetime(2026, 3, 4, 12, 55, 18, 932895, tzinfo=utc)))])),
                ('completed_state', models.CharField(choices=[('In progress', 'In progress'), ('Completed', 'Completed'), ('Overdue', 'Overdue')], default='In Progress', max_length=30)),
                ('priority_state', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low', max_length=30)),
                ('work_or_leisure', models.CharField(choices=[('Work', 'Work'), ('Leisure', 'Leisure')], default='leisure', max_length=30)),
                ('description', models.TextField(blank=True)),
                ('title', models.CharField(max_length=200)),
                ('budget', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('travel_required', models.BooleanField(default=False)),
                ('entertainment', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_task', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]