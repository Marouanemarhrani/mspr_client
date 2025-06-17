from django.urls import path
from ptk_client.views.register_view import register_client

from ptk_client.views.login_view import login_client

urlpatterns = [
    path('register/', register_client, name='register-client'),
    path('login/', login_client, name='login-client'),
]
