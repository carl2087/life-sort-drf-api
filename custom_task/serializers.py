"""
Serializer for the custom task model
"""
from django.utils import timezone
from rest_framework import serializers
from .models import CustomTask
from django.utils import timezone


class CustomTaskSerializer(serializers.ModelSerializer):
    """
    Class to serailize the custom task model information returned from
    the database. Adds extra fields displaying the id of the
    custom task, who owns the custom task and whether the user is the owner
    of the custom task
    """
    id = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    is_overdue = serializers.SerializerMethodField()
    due_date = serializers.DateTimeField()
    start_date = serializers.DateTimeField()

    def validate(self, data):
        """
        Validates the dates entered ensuring that they are in future and 
        start date cannot be set before due date
        """
        if data['due_date'] < timezone.now() + timezone.timedelta(
                days=1):
            raise serializers.ValidationError(
                "Due date must be at least 24 hours in future")
        elif data['due_date'] > timezone.now() + timezone.timedelta(
                days=1000):
            raise serializers.ValidationError(
                "Due date cannot be more than 1000 days in future")
        elif data['start_date'] < timezone.now() + timezone.timedelta(
                days=1):
            raise serializers.ValidationError(
                    "Start date must be at least 24 hours in future"
                )
        elif data['start_date'] > timezone.now() + timezone.timedelta(
                days=1000):
            raise serializers.ValidationError(
                    "Start date cannot be more than 1000 days in future"
                )
        elif data['due_date'] < data['start_date']:
            raise serializers.ValidationError(
                "Due date must be after start date.")
        return data

    def get_is_owner(self, obj):
        """
        returns whether the logged in user is the owner of the custom task
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_is_overdue(self, obj):
        """
        returns whether the current custom task is overdue or not
        """
        now = timezone.now()
        if obj.due_date < now:
            return True
        else:
            return False

    class Meta:
        model = CustomTask
        fields = [
            'id', 'owner', 'date_created', 'date_updated', 'due_date',
            'start_date', 'completed_state', 'priority_state',
            'work_or_leisure', 'title', 'description', 'travel_required',
            'entertainment', 'is_owner', 'is_overdue', 'budget'
        ]
