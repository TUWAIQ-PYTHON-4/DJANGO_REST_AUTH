from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import UserSerializer


@api_view(['POST'])
def register(request: Request):
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        new_user = User.objects.create_user(**user_serializer.data)
        new_user.save()
        return Response({"msg": f"{new_user.username} hase been created"})
    else:
        return Response({"msg": "Couldn't create a user"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login(request : Request):

    if 'username' in request.data and 'password' in request.data:
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user:
            token = AccessToken.for_user(user)
            responseData = {
                "msg": "Your token have been generated",
                "token": str(token)
            }
            return Response(responseData)




