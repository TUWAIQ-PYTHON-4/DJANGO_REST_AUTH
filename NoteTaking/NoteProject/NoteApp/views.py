from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import NoteModel
from .serializers import NoteModelSerializer


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_note(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_note = NoteModelSerializer(data=request.data)
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
    note_list = NoteModel.objects.all()

    dataResponse = {
        "msg" : "List of All note",
        "note" : NoteModelSerializer(instance=note_list, many=True).data
    }

    return Response(dataResponse)


@api_view(['PUT'])
def update_note(request : Request, note_id):
    up_note = NoteModel.objects.get(id=note_id)

    updated_note = NoteModelSerializer(instance=up_note, data=request.data)
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
    del_not = NoteModel.objects.get(id=note_id)
    del_not.delete()
    return Response({"msg" : "Deleted Successfully"})