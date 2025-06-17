from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Client
        fields = [
            'id',         # UUID
            'email',
            'nom',
            'prenom',
            'telephone',
            'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return Client.objects.create_user(**validated_data)
