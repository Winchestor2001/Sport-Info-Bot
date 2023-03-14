from rest_framework import serializers
from .models import *


class GetUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = ['user_id']


class LigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liga
        fields = '__all__'


class LigaTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigaTable
        fields = '__all__'


class LigaPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigaPlayer
        fields = '__all__'


class TopTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopTeam
        fields = '__all__'


class LigaCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameCalendar
        fields = '__all__'

