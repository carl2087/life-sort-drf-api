from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Holiday(models.Model):
    """
    Holiday model, related to 'owner' ie a User instance.
    Minimum requirement set for date of holiday to be today plus one day
    budget defaults to zero and no minus allowed
    """
    COMPLETED_STATE_CHOICES = [
        ('In progress', 'In progress'),
        ('Completed', 'Completed')
    ]
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='holiday')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_of_holiday = models.DateTimeField(
        blank=False, validators=[MinValueValidator(
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
        default='In progress'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    budget = models.IntegerField(
        blank=False, default=0, validators=[MinValueValidator(0)])
    clothes = models.BooleanField(default=False)
    passport = models.BooleanField(default=False)
    holiday_insurance = models.BooleanField(default=False)
    suitcases_packed = models.BooleanField(default=False)
    holiday_paid_in_full = models.BooleanField(default=False)
    car_hire = models.BooleanField(default=False)
    tickets = models.BooleanField(default=False)
    entertainment = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_of_holiday']

    def __str__(self):
        return f'{self.title}'
