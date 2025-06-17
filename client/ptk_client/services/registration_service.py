from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import IntegrityError
from ptk_client.serializers import ClientSerializer
from ptk_client.rabbitmq import publish_client_created  # <-- RabbitMQ ici

def register_client_service(data):
    serializer = ClientSerializer(data=data)

    if not serializer.is_valid():
        return Response({
            "message": "Erreur de validation.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        client = serializer.save()
        refresh = RefreshToken.for_user(client)

        # 🐰 RabbitMQ : publier "ClientCreated"
        publish_client_created({
            "id": str(client.id),
            "email": client.email,
            "nom": client.nom,
            "prenom": client.prenom,
            "telephone": client.telephone
        })

        return Response({
            "message": "Inscription réussie.",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "email": client.email
        }, status=status.HTTP_201_CREATED)

    except IntegrityError:
        return Response({
            "message": "Un utilisateur avec cet email existe déjà."
        }, status=status.HTTP_409_CONFLICT)

    except Exception as e:
        return Response({
            "message": "Erreur inattendue.",
            "details": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
