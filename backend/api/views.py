from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import GetUsersSerializer, LigaTableSerializer, LigaPlayerSerializer, TopTeamSerializer, \
    LigaSerializer, LigaCalendarSerializer


class UserAPIView(APIView):
    def get(self, request):
        users = TgUser.objects.all()
        serializer = GetUsersSerializer(users, many=True).data
        return Response(serializer)

    def post(self, request):
        TgUser.objects.update_or_create(
            user_id=request.POST.get('user_id'),
            username=request.POST.get('username')
        )
        return Response(status=200)


class LigaTableAPIView(APIView):
    def get(self, request):
        return Response(status=200)

    def post(self, request):
        team = LigaTable.objects.filter(team=request.data['team']).first()
        serializer = LigaTableSerializer(data=request.data, instance=team)
        if serializer.is_valid():
            serializer.save()
        return Response(status=200)


class LigaPlayerAPIView(APIView):
    def get(self, request):
        return Response(status=200)

    def post(self, request):
        player = LigaPlayer.objects.filter(player=request.data['player']).first()
        serializer = LigaPlayerSerializer(data=request.data, instance=player)
        if serializer.is_valid():
            serializer.save()
        return Response(status=200)


class TopTeamAPIView(APIView):
    def get(self, request):
        return Response(status=200)

    def post(self, request):
        team = TopTeam.objects.filter(team=request.data['team']).first()
        serializer = TopTeamSerializer(data=request.data, instance=team)
        if serializer.is_valid():
            serializer.save()
        return Response(status=200)


class LigaAPIView(APIView):
    def get(self, request):
        ligas = Liga.objects.all()
        serializer = LigaSerializer(ligas, many=True).data
        return Response(serializer, status=200)


class LigaCalendarAPIView(APIView):
    def get(self, request):
        return Response(status=200)

    def post(self, request):
        team = GameCalendar.objects.filter(tour=request.data['tour']).first()
        serializer = LigaCalendarSerializer(data=request.data, instance=team)
        if serializer.is_valid():
            serializer.save()
        return Response(status=200)


