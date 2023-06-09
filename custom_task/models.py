from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomTask(models.Model):
    """
    Custom task model related to 'owner' ie a User instance.
    Minimum requirement set for due date of task to be today plus one day
    Minimum requirement set for start date of task to be today plus one day
    """
    COMPLETED_STATE_CHOICES = [
        ('In progress', 'In progress'),
        ('Completed', 'Completed'),
        ('Overdue', 'Overdue'),
    ]

    PRIORITY_STATE_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    WORK_OR_LEISURE_CHOICES = [
        ('Work', 'Work'),
        ('Leisure', 'Leisure')
    ]

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='custom_task')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(
        blank=False, validators=[MinValueValidator(
            timezone.now() + timezone.timedelta(
                days=1
            )),
            MaxValueValidator(timezone.now() + timezone.timedelta(
                days=1000
            ))
        ]
    )
    start_date = models.DateTimeField(
        validators=[MinValueValidator(
            timezone.now() + timezone.timedelta(
                days=1
            ),
            MaxValueValidator(timezone.now() + timezone.timedelta(
                days=1000
            ))
        )]
    )
    completed_state = models.CharField(
        max_length=30, choices=COMPLETED_STATE_CHOICES,
        default='In Progress'
    )
    priority_state = models.CharField(
        max_length=30, choices=PRIORITY_STATE_CHOICES,
        default='Low',
    )
    work_or_leisure = models.CharField(
        max_length=30, choices=WORK_OR_LEISURE_CHOICES,
        default='leisure',
    )
    description = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    budget = models.IntegerField(
        blank=False, default=0, validators=[MinValueValidator(0)])
    travel_required = models.BooleanField(default=False)
    entertainment = models.BooleanField(default=False)
