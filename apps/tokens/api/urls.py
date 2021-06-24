from django.urls import path
from apps.tokens.api.api import token_api_view

urlpatterns = [
    path('token/',token_api_view, name = 'token_api')
]