from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth.models import User
from .models import Note
from .serializers import UserRegisterSerializer, NoteSerializer


# Create your views here.
@api_view(['POST'])
def register_user(request: Request):
    user_serializer = UserRegisterSerializer(data=request.data)
    if user_serializer.is_valid():
        new_user = User.objects.create_user(**user_serializer.data)
        new_user.save()
        return Response({'msg': 'created user successfully'})
    else:
        print(user_serializer.errors)
        return Response({'msg': 'Could not create suer'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request: Request):
    if 'username' in request.data and 'password' in request.data:
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user is not None:
            token = AccessToken.for_user(user)
            responseData = {
                'msg': 'Your token is ready',
                'token': str(token)
            }
            return Response(responseData)
    return Response({'msg': 'Provide your username and password'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_note(request: Request):
    if not request.user.is_authenticated:
        return Response({'msg': 'Not Allowed'}, status=status.HTTP_401_UNAUTHORIZED)

    note = NoteSerializer(data=request.data)
    if note.is_valid():
        note.save()
        dataResponse = {
            'msg': 'Note Added Successfully',
            'note': note.data
        }
        return Response(dataResponse)
    else:
        print(note.errors)
        dataResponse = {'msg': 'Unable to add note'}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_notes(request: Request):
    note = Note.objects.all()
    dataResponse = {
        'msg': 'List of All Notes',
        'Note': NoteSerializer(instance=note, many=True).data
    }
    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_note(request: Request, note_id):
    if not request.user.is_authenticated:
        return Response({'msg': 'Not Allowed'}, status=status.HTTP_401_UNAUTHORIZED)

    note = Note.objects.get(id=note_id)
    note_updated = NoteSerializer(instance=note, data=request.data)
    if note_updated.is_valid():
        note_updated.save()
        responseData = {
            'msg': 'Note Updated Successfully'
        }
        return Response(responseData)
    else:
        print(note_updated.errors)
        return Response({'msg': 'bad request, Unable to update'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_note(request: Request, note_id):
    if not request.user.is_authenticated:
        return Response({'msg': 'Not Allowed'}, status=status.HTTP_401_UNAUTHORIZED)
    note = Note.objects.get(id=note_id)
    note.delete()
    return Response({'msg': 'Note Deleted Successfully'})
