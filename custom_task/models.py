from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


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
    due_date = models.DateTimeField()
    start_date = models.DateTimeField()
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
        default='Leisure',
    )
    description = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    budget = models.IntegerField(
        blank=False, default=0, validators=[MinValueValidator(0)])
    travel_required = models.BooleanField(default=False)
    entertainment = models.BooleanField(default=False)

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return f'{self.title}'
