from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)


"""
Welcome message displayed to users when visiting the API.
"""


@api_view()
def root_route(request):
    return Response({
        'message': "Welcome to the Life sort API!"
    })
