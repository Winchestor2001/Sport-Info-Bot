from rest_framework import serializers
from .models import *


class GetUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = ['user_id']
