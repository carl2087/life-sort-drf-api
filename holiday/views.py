from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Holiday
from .serializers import HolidaySerializer


class HolidayList(APIView):
    def get(self, request):
        holidays = Holiday.objects.all()
        serializer = HolidaySerializer(
            holidays, many=True, context={'request': request}
        )
        return Response(serializer.data)
