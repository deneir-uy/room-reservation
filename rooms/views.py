from rest_framework import viewsets
from .models import Room
from .serializers import RoomSerializer


class RoomList(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetail(viewsets.ModelViewSet):
    # queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.filter(pk=self.kwargs['pk'])

