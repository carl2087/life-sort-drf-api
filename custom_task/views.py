"""
Renders the custom task view for the API
"""
from django.http import Http404
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomTask
from .serializers import CustomTaskSerializer
from life_sort_api.permissions import IsOwnerOrReadOnly


class CustomTaskList(generics.ListCreateAPIView):
    serializer_class = CustomTaskSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = CustomTask.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = [
        'completed_state',
        'priority_state', 'title', 'description', 'work_or_leisure']
    search_fields = [
        'completed_state',
        'priority_state', 'title', 'description', 'work_or_leisure']

    def perform_create(self, serializer):
        """
        saves a new custom task to the database
        """
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Makes it so only the custom tasks that the user owns are available.
        Q object makes it so an anonymous user cannot retrieve any
        information from the list view.
        """
        if self.request.user.is_anonymous:
            return self.queryset.filter(Q(pk=None))
        else:
            return self.queryset.filter(owner=self.request.user)
