from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from ptk_client.serializers import ClientSerializer

def login_client_service(data, context=None):
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return Response({
            "message": "Email et mot de passe requis."
        }, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(email=email, password=password)

    if not user:
        return Response({
            "message": "Identifiants incorrects."
        }, status=status.HTTP_401_UNAUTHORIZED)

    if not user.is_active:
        return Response({
            "message": "Ce compte n’est pas activé."
        }, status=status.HTTP_403_FORBIDDEN)

    refresh = RefreshToken.for_user(user)
    user_data = ClientSerializer(user).data

    return Response({
        "message": "Connexion réussie.",
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "user": user_data
    }, status=status.HTTP_200_OK)
