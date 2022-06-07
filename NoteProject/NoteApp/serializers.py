from rest_framework import serializers
from .models import NoteInfo

class NoteInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoteInfo
        fields = '__all__'