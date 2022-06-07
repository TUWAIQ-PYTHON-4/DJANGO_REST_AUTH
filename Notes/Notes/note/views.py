from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Notes
from .serializers import NotesSerializer


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_note(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_note = NotesSerializer(data=request.data)
    if new_note.is_valid():
        new_note.save()
        dataResponse = {
            "msg": "Created Successfully",
            "note": new_note.data
        }
        return Response(dataResponse)
    else:
        print(new_note.errors)
        dataResponse = {"msg": "couldn't create a new note"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_note(request: Request):
    notes = Notes.objects.all()

    dataResponse = {
        "msg": "List of Notes:",
        "Notes": NotesSerializer(instance=notes, many=True).data
    }

    return Response(dataResponse)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def update_note(request: Request, notes_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    note = Notes.objects.get(id=notes_id)

    updated_note = NotesSerializer(instance=note, data=request.data)
    if updated_note.is_valid():
        updated_note.save()
        responseData = {
            "msg": "updated successfully"
        }

        return Response(responseData)
    else:
        print(updated_note.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_note(request: Request, notes_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    student = Notes.objects.get(id=notes_id)
    student.delete()
    return Response({"msg": "Deleted Successfully"})
