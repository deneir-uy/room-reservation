from rest_framework import viewsets
from .models import Room
from django.contrib.auth.models import User
from .serializers import RoomSerializer, ReservationSerializer


class RoomList(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetail(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ReservationCreate(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(user=User.objects.get(pk=self.request.user.id), room=Room.objects.get(pk=self.kwargs['pk']))

    queryset = Room.objects.all()
    serializer_class = ReservationSerializer
