from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.contrib.auth.models import User

@api_view(['POST'])
def add_note(request : Request, user_id):
    try:
      user = User.objects.get(pk=user_id)
      if User.is_authenticated and User.has_perm('NoteTakingApp.add_note'):
          new_note = NoteSerializer(user=user, title=request.data['title'], content=request.data['content'])
          if new_note.is_valid():
             new_note.save()
             dataResponse = {
               "msg" : "Note added Successfully",
               "Note" : new_note.data
             }
             return Response(dataResponse)
          else:
            dataResponse = {"msg" : "couldn't add a note"}
            return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)
      else:
        dataResponse = {"msg": "UNAUTHORIZED"}
        return Response(dataResponse, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        print(e)




@api_view(['GET'])
def list_note(request : Request):
    notes = Note.objects.all()

    dataResponse = {
        "msg" : "List of All notes",
        "students" : NoteSerializer(instance=notes, many=True).data
    }

    return Response(dataResponse)

@api_view(['PUT'])
def update_note(request : Request, note_id):
    note = Note.objects.get(id=note_id)
    if User.is_authenticated and User.has_perm('NoteTakingApp.change_note'):
      updated_note = NoteSerializer(instance=note, data=request.data)
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
def delete_note(request: Request, note_id):
  if User.is_authenticated and User.has_perm('NoteTakingApp.delete_note'):
    note = Note.objects.get(id=note_id)
    note.delete()
    return Response({"msg" : "Deleted Successfully"})



