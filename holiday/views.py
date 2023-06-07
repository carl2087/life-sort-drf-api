from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Holiday
from .serializers import HolidaySerializer


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
