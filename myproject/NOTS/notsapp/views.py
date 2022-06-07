from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view ,authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
# Create your views here.
from .models import Notes
from .seri import NotesSeri
from rest_framework_simplejwt.authentication import JWTAuthentication

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_note (request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_note = NotesSeri(data=request.data)
    if new_note.is_valid():
        new_note.save()
        dataResponse = {
            "msg": "Created Successfully",
            "note": new_note.data
        }
        return Response(dataResponse)
    else:
        print(new_note.errors)
        dataResponse = {"msg": "couldn't create a Note"}
        return Response(dataResponse)

@api_view(['GET'])
def list_note(request:Request):
    note = Notes.objects.all()

    dataResponse = {
        "msg": " List of All Notes ",
        "Notes": NotesSeri(instance=note, many=True).data
    }

    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def put_note(request:Request , note_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    note = Notes.objects.get(id=note_id)
    putNote = NotesSeri(instance=note, data=request.data)
    if putNote.is_valid():
        putNote.save()
        responseData = {
            "msg": "updated successefully"
        }

        return Response(responseData)
    else:
        print(putNote.errors)
        return Response({"msg": "bad request, cannot update"})


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_note (request:Request , note_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    note = Notes.objects.get(id=note_id)
    note.delete()
    return Response({"msg": "Deleted Successfully"})


