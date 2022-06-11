from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_routs(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]
    return Response(routes)
