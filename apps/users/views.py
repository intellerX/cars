from django.contrib.sessions.models import Session
import jwt
from datetime import datetime
from datetime import timedelta
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from apps.tokens.models import Token
from django.contrib.auth.hashers import check_password
from apps.users.models import User

from apps.users.api.serializers import UserSerializer
from django.conf import settings




class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.data['username']).first()
        if not user:
            return Response({'error': 'usuario no existe'}, status=status.HTTP_404_NOT_FOUND)
        if not check_password(request.data['password'], user.password):
            return Response({'error': 'contraseña incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)

        token = jwt.encode({
            "expiration_date": str(datetime.now() + timedelta(hours=2)),
            "username": user.username,
            "is_admin": user.is_staff            
            }, settings.SECRET_KEY,algorithm='HS256')

        Token.objects.create( name = ('admin' if user.is_staff else 'client'),token = token)
        return Response({"token": token}, status=status.HTTP_201_CREATED)

        


"""





        login_serializer = self.serializer_class(
            data=request.data, context={'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']

            if user.is_staff:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Login Exitoso'

                    }, status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(
                        expire_date__gte=datetime.datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Login Exitoso'
                    }, status.HTTP_201_CREATED)

        else:
            return Response({'error': 'Nombre de usuario o contraseña incorrectos.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"peticion realizada"}, status=status.HTTP_200_OK)
"""