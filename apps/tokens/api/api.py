from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.tokens.api.serializers import TokenSerializer
from apps.tokens.models import Token

@api_view(['GET','POST'])
def token_api_view(request):

    if request.method == 'GET:':
        tokens = Token.objects.all()
        tokens_serializer = TokenSerializer(tokens,many = True)
        return Response(tokens_serializer.data)

    elif request.method == 'POST':
        tokens_serializer = TokenSerializer(data = request.data)
        if tokens_serializer.is_valid():
            tokens_serializer.save()
            return Response(tokens_serializer.data)
        return Response(tokens_serializer.errors)
