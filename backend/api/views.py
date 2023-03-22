from django.core import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import GetUsersSerializer, LigaTableSerializer, LigaPlayerSerializer, TopTeamSerializer, \
    LigaSerializer, LigaCalendarSerializer, GetTeamsSerializer


class UserAPIView(APIView):
    def get(self, request):
        users = TgUser.objects.all()
        serializer = GetUsersSerializer(users, many=True).data
        return Response(serializer)

    def post(self, request):
        user = TgUser.objects.update_or_create(
            user_id=request.POST.get('user_id'),
            username=request.POST.get('username')
        )
        serializer = GetUsersSerializer(data=user, instance=user)
        if serializer.is_valid():
            serializer.save()
        return Response(status=200)


class GetUserInfoAPIView(APIView):
    def get(self, request):
        user_id = request.data.get('user_id')
        user = TgUser.objects.get(user_id=user_id)
        serializer = GetUsersSerializer(user).data
        return Response(serializer, status=200)

    def post(self, request):
        user_id = request.data.get('user')
        team = request.data.get('team')
        user = TgUser.objects.get(user_id=user_id)
        user.team = team
        user.save()
        return Response(status=200)

    def put(self, request):
        user = request.data.get('user')
        lang = request.data.get('lang')
        user = TgUser.objects.get(user_id=user)
        user.language = lang
        user.save()
        return Response(status=200)


class LigaTableAPIView(APIView):
    def get(self, request):
        liga = Liga.objects.get(pk=request.data.get('liga'))
        liga = str(liga.name).lower()
        teams = LigaTable.objects.filter(liga__contains=liga)
        serializer = LigaTableSerializer(data=teams, many=True)
        serializer.is_valid()
        return Response({'liga': liga, 'data': serializer.data}, status=200)

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
        teams = TopTeam.objects.all()
        serializer = TopTeamSerializer(data=teams, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=200)

    def post(self, request):
        team = TopTeam.objects.filter(team=request.data['team']).first()
        serializer = TopTeamSerializer(data=request.data, instance=team)
        if serializer.is_valid():
            serializer.save()
        return Response(status=200)


class LigaAPIView(APIView):
    def get(self, request):
        ligas = Liga.objects.filter(is_active=True)
        serializer = LigaSerializer(ligas, many=True).data
        return Response(serializer, status=200)


class LigaCalendarAPIView(APIView):
    def get(self, request):
        liga = Liga.objects.get(pk=request.data.get('liga'))
        liga = str(liga.name).lower()
        tours = GameCalendar.objects.filter(liga__contains=liga)
        serializer = LigaCalendarSerializer(data=tours, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=200)

    def post(self, request):
        GameCalendar.objects.get(tour=request.data.get('tour'), team=request.data.get('team')).delete()
        serializer = LigaCalendarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=200)


class GetTeamsAPIView(APIView):
    def get(self, request):
        teams = LigaTable.objects.all()
        serializer = GetTeamsSerializer(data=teams, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=200)


class GetLigaTourAPIView(APIView):
    def post(self, request):
        liga = Liga.objects.get(pk=request.POST.get('liga'))
        liga = str(liga.name).lower()
        tour = request.POST.get('tour')
        liga_tour = GameCalendar.objects.filter(liga=liga, tour=tour)
        serializer = serializers.serialize('json', liga_tour)
        return Response(serializer, status=200)
