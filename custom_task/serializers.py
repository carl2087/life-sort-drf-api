"""
Serializer for the custom task model
"""
from django.utils import timezone
from rest_framework import serializers
from .models import CustomTask


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

    class Meta:
        model = CustomTask
        fields = [
            'id', 'owner', 'date_created', 'date_updated', 'due_date',
            'start_date', 'completed_state', 'priority_state', 'work_or_leisure',
            'title', 'description', 'travel_required', 'entertainment',
            'is_owner', 'is_overdue'
        ]
