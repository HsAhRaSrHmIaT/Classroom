from rest_framework.response import Response #type: ignore
from rest_framework.decorators import api_view #type: ignore
from classroomApp.models import Room #type: ignore
from .serializers import RoomSerializer #type: ignore

@api_view(["GET"])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]

    return Response({"message": "Welcome to the API", "routes": routes})

@api_view(["GET"])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)


