from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import  NoteInfo
from .serializers import NoteInfoSerializer




@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_note(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_note = NoteInfoSerializer(data=request.data)
    if new_note.is_valid():
        new_note.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "note" : new_note.data
        }
        return Response(dataResponse)
    else:
        print(new_note.errors)
        dataResponse = {"msg" : "couldn't create a Note"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
def list_notes(request : Request):
    notes = NoteInfo.objects.all()

    dataResponse = {
        "msg" : "List of All cities",
        "notes" : NoteInfoSerializer(instance=notes, many=True).data
    }

    return Response(dataResponse)



@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_note(request : Request, note_id):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    note = NoteInfo.objects.get(id=note_id)

    uptade_note = NoteInfoSerializer(instance=note, data=request.data)
    if uptade_note.is_valid():
        uptade_note.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(uptade_note.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_note(request: Request, note_id):
   
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    notes = NoteInfo.objects.get(id=note_id)
    notes.delete()
    return Response({"msg" : "Deleted Successfully"})
