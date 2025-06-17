from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from ptk_client.services.login_service import login_client_service

@api_view(['POST'])
@permission_classes([AllowAny])
def login_client(request):
    return login_client_service(request.data, context={'request': request})
