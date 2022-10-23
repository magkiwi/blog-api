from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login

from blog.serializers.user import UserSerializer


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = dict(attrs)

        refresh = self.get_token(data['email'])

        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data