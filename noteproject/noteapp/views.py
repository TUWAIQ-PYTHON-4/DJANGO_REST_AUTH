from os import stat
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import note
from .serializers import NoteSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def create_note(request : Request):

    new_note = NoteSerializer(data=request.data)
    if new_note.is_valid():
        new_note.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "note" : new_note.data
        }
        return Response(dataResponse)
    else:
        print(new_note.errors)
        dataResponse = {"msg" : "couldn't create a note"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_note(request : Request):
    students = note.objects.all()

    dataResponse = {
        "msg" : "List of All nots",
        "note" : NoteSerializer(instance=students, many=True).data
    }

    return Response(dataResponse)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_note(request : Request, note_id):
    note_update = note.objects.get(id=note_id)

    updated_note = NoteSerializer(instance=note_update, data=request.data)
    if updated_note.is_valid():
        updated_note.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_note.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_note(request: Request, note_id):
    note_dalete = note.objects.get(id=note_id)
    note_dalete.delete()
    return Response({"msg" : "Deleted Successfully"})