from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Holiday
from .serializers import HolidaySerializer
from life_sort_api.permissions import IsOwnerOrReadOnly


class HolidayList(APIView):
    serializer_class = HolidaySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        holidays = Holiday.objects.all()
        serializer = HolidaySerializer(
            holidays, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = HolidaySerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HolidayDetail(APIView):
    serializer_class = HolidaySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            holiday = Holiday.objects.get(pk=pk)
            self.check_object_permissions(self.request, holiday)
            return holiday
        except Holiday.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        holiday = self.get_object(pk)
        serializer = HolidaySerializer(
            holiday, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        holiday = self.get_object(pk)
        serializer = HolidaySerializer(
            holiday, data=request.data, context={
                'request': request
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        holiday = self.get_object(pk)
        holiday.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
