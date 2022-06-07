from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def create_note(request : Request):
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

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
        return Response( {"msg" : "couldn't create a note"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def list_notes(request : Request):
    notes = Note.objects.all()
    notes_list = NoteSerializer(instance=notes, many=True).data
    dataResponse = {
        "msg": "List of All Notes",
        "notes": notes_list
    }
    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def edit_note(request: Request,note_id):
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    note = Note.objects.get(id=note_id)
    edited_note = NoteSerializer(instance=note, data=request.data)
    if edited_note.is_valid():
        edited_note.save()
        dataResponse = {
            "msg": "Edited Note Successfully",
        }
        return Response(dataResponse)
    else:
        print(edited_note.errors)
        return Response({"msg": "couldn't edit the note"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def remove_note(request: Request, note_id):
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    note = Note.objects.get(id=note_id)
    note.delete()
    return Response({"msg" : "Removed Note Successfully"})

