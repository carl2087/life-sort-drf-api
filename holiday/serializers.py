"""
Serializer for the holiday model
"""
from django.utils import timezone
from rest_framework import serializers
from .models import Holiday


class HolidaySerializer(serializers.ModelSerializer):
    """
    Class to serialize holiday information returned from
    database. Adds extras fields displaying the id of the
    holiday, who owns the specific holiday and whether the
    user is the owner of the holiday.
    """
    id = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    date_of_holiday = serializers.DateTimeField()

    def validate(self, data):
        """
        Validates the date set on date of holiday ensuring it is 
        in the future and not more than 1000 days in future
        """

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Holiday
        fields = [
            'id', 'owner', 'date_created', 'date_updated', 'date_of_holiday',
            'completed_state', 'title', 'description', 'budget', 'clothes',
            'passport', 'holiday_insurance', 'suitcases_packed',
            'holiday_paid_in_full', 'car_hire', 'tickets', 'entertainment',
            'is_owner'
        ]
