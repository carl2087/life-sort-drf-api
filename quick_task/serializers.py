"""
Serializer for the quick task model
"""
from django.utils import timezone
from rest_framework import serializers
from .models import QuickTask


class QuickTaskSerializer(serializers.ModelSerializer):
    """
    Class to serailize the quick task model information returned from
    the database. Adds extra fields displaying the id of the
    quick task, who owns the quick task and whether the user is the owner
    of the quick task
    """
    id = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    is_overdue = serializers.SerializerMethodField()
    due_date = serializers.DateTimeField()

    def validate(self, data):
        """
        Validates the date set on due date ensuring it is
        in the future and not more than 1000 days in future
        """
        if data['due_date'] < timezone.now() + timezone.timedelta(
                days=1):
            raise serializers.ValidationError(
                "Due date must be at least 24 hours in future")
        elif data['due_date'] > timezone.now() + timezone.timedelta(
                days=1000):
            raise serializers.ValidationError(
                "Due date cannot be more than 1000 days in future")
        return data

    def get_is_owner(self, obj):
        """
        returns whether the logged in user is the owner of the quick task
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_is_overdue(self, obj):
        """
        returns whether the current quick task is overdue or not
        """
        now = timezone.now()
        if obj.due_date < now:
            return True

    class Meta:
        model = QuickTask
        fields = [
            'id', 'owner', 'date_created', 'date_updated', 'due_date',
            'completed_state', 'priority_state', 'title', 'description',
            'is_owner', 'is_overdue'
        ]
