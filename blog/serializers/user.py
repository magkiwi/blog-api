from rest_framework import serializers
from blog.models import User
from blog.serializers.group import GroupSerializer
from django.contrib.auth.models import Group, update_last_login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ["id"]
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "groups",
            "permissions"
        ]
    groups = GroupSerializer()
    permissions = serializers.SerializerMethodField()

    def get_permissions(self, instance):
        user_types = instance.groups
        if user_types:
            group_permissions = Group.objects.get(id=user_types.pk).permissions
            all_permissions = [permissions['codename'] for permissions in group_permissions.values()]
            return all_permissions