"""
Renders the quick task view for the API
"""
from django.http import Http404
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import QuickTask
from .serializers import QuickTaskSerializer
from life_sort_api.permissions import IsOwnerOrReadOnly


class QuickTaskList(generics.ListCreateAPIView):
    serializer_class = QuickTaskSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = QuickTask.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = [
        'due_date', 'completed_state',
        'priority_state', 'title', 'description']
    search_fields = [
        'due_date', 'completed_state',
        'priority_state', 'title', 'description']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Makes it so only the quick tasks that the user owns are available.
        Q object makes it so an anonymous user cannot retrieve any
        information from the list view.
        """
        if self.request.user.is_anonymous:
            return self.queryset.filter(Q(pk=None))
        else:
            return self.queryset.filter(owner=self.request.user)
