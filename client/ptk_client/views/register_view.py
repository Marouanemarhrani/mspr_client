from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from ptk_client.services.registration_service import register_client_service

@api_view(['POST'])
@permission_classes([AllowAny])
def register_client(request):
    return register_client_service(request.data)
