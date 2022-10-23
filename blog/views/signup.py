from rest_framework import generics
from rest_framework.response import Response

from blog.exceptions.user_create_exception import UserCreationException
from blog.repositories.signup import SignupRepository
from blog.serializers.signup import SignupSerializer


class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        try:
            SignupRepository().signup(validated_data)
            return Response(status=201)
        except UserCreationException as exc:
            return Response(exc.args[0], status=400)
