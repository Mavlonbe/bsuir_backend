from rest_framework.serializers import ModelSerializer, Serializer, CharField, ListField
from .models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class EventSerializer(Serializer):
    EventType = CharField(max_length=200)
    
    Message = ListField(
        child=CharField(max_length=200)
    )
    
    