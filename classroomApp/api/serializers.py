from rest_framework.serializers import ModelSerializer #type: ignore
from classroomApp.models import Room #type: ignore

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"