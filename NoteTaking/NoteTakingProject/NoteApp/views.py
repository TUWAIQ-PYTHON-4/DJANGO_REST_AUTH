from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import NoteModel
from .serializers import NoteSerializer

from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_new_note(request : Request ):
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_note = NoteSerializer(data=request.data)
    if new_note.is_valid():
        new_note.save()
        Note = {
            "message" : "Created Successfully , Done ",
            "Note" : new_note.data
                 }
        return Response(Note)
    else:
        print(new_note.errors)
        Note = {"message" : "Sorry, this Note cannot be Added !!"}
        return Response(Note, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def notes_show(request : Request):
    notes = NoteModel.objects.all()

    Note = {
        "message": "Notes Taking :",
        "notes" : NoteSerializer(instance=notes , many=True).data
    }
    return Response(Note)
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_note(request : Request, note_id ):
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    note_get = NoteModel.objects.get(id = note_id)
    edit_note = NoteSerializer(instance=note_get ,data=request.data)
    if edit_note.is_valid():
        edit_note.save()
        note ={
            "message": "updated successefully"
        }
        return Response(note)
    else:
        print(edit_note.errors)
        return Response( {"message":"bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_note(request: Request, note_id):
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    note = NoteModel.objects.get(id=note_id)
    note.delete()
    return Response({"message": "Deleted Note Successfully"})
