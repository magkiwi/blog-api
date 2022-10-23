import jwt
from django.http import Http404
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

import settings
from blog.models import User
from blog.serializers.user import UserSerializer


class UserMeView(generics.RetrieveAPIView):
    permission_classes = ()
    serializer_class = UserSerializer

    def get_object(self):
        try:
            user_instance = User.objects.get(id=self.request.user.id)
            return user_instance
        except:
            raise Http404()

