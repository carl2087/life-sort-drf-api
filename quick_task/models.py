from django.db import models
from django.contrib.auth.models import User


class QuickTask(models.Model):
    """
    Quick task model. related to 'owner' ie a User instance.
    Minimum requirement set for due date of task to be today plus one day
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

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='quick_task')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    completed_state = models.CharField(
        max_length=30, choices=COMPLETED_STATE_CHOICES,
        default='In Progress'
    )
    priority_state = models.CharField(
        max_length=30, choices=PRIORITY_STATE_CHOICES,
        default='Low',
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return f'{self.title}'
