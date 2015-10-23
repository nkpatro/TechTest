from django.contrib.auth.models import User, Group
from rest_framework import serializers

__author__ = 'npatro'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_superuser',
                  'first_name', 'last_name', 'is_staff', 'is_active',
                  'groups')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
