from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class SignupSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=1024)
    repeated_password = serializers.CharField(max_length=1024)
    first_name = serializers.CharField(max_length=1024, required=False)
    last_name = serializers.CharField(max_length=1024, required=False)
    email = serializers.CharField(max_length=1024)

    def validate(self, data):
        if "password" and "repeated_password" in data:
            if data["password"] != data["repeated_password"]:
                raise serializers.ValidationError(
                    {"password": "Provided passwords don't match"}
                )
        data["password"] = make_password(data["password"])
        return data
