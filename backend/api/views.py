from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import GetUsersSerializer


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




