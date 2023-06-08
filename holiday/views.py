"""
Renders the holiday view for the API
"""
from django.http import Http404
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Holiday
from .serializers import HolidaySerializer
from life_sort_api.permissions import IsOwnerOrReadOnly


class HolidayList(generics.ListCreateAPIView):
    serializer_class = HolidaySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Holiday.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['title', 'description',]
    search_fields = ['title', 'description', 'completed_state']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Makes it so only the holiday tasks that the user owns are available.
        Q object makes it so an anonymous user cannot retrieve any
        information from the list view.
        """
        if self.request.user.is_anonymous:
            return self.queryset.filter(Q(pk=None))
        else:
            return self.queryset.filter(owner=self.request.user)


class HolidayDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsOwnerOrReadOnly
    ]
    serializer_class = HolidaySerializer
    queryset = Holiday.objects.all()
