import datetime

from django.utils.baseconv import base64
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

import settings
from blog.exceptions.user_not_exists import UserNotExists
from blog.models import User
from django.http import Http404
from blog.serializers.user import UserSerializer
import jwt, datetime





class LogInView(APIView):

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
            user = User.objects.filter(email=email).first()

            if user is None:
                raise AuthenticationFailed('User not found')

            if not user.check_password(password):
                raise AuthenticationFailed('Incorrect password')

            generate_access_token = self.get_tokens_for_user(user)
            return Response({"response": True, "return_code": "login_success", 'tokens': generate_access_token})



            return Response({
                'jwt': access_token_payload
            })
        except UserNotExists as e:
            raise Http404(e.args[0])
