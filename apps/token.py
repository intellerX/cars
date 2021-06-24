import jwt
from django.conf import settings
from datetime import datetime

from .users.models import User
from .tokens.models import Token


class TokenHandler:
    def get_payload(self,request):
        header = request.headers.get("Authorization", None)
        if (not header or len(header.split(" ")) != 2 or
                header.split(" ")[0].lower() != "bearer"):
            return None, None

        try:
            token = jwt.decode(header.split(
                " ")[1], settings.SECRET_KEY, algorithms='HS256')
        except jwt.InvalidTokenError:
            return None, None

        expiration_date = datetime.strptime(token['expiration_date'],
            '%Y-%m-%d %H:%M:%S.%f')

        db_token = Token.objects.filter(token=header.split(" ")[1]).first()

        if (expiration_date < datetime.now() or not db_token):
            return None, None

        user = User.objects.filter(
            username=token["username"], is_active=True).first()

        if not user:
            return None, None

        return token, user
    pass
