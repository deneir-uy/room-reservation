from rest_framework import generics
from .models import Room, Reservation, User
from .serializers import RoomSerializer, ReservationSerializer


class RoomList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetail(generics.RetrieveUpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ReservationCreate(generics.CreateAPIView):
    def perform_create(self, serializer):
        serializer.save(user=User.objects.get(pk=self.request.user.id), room=Room.objects.get(pk=self.kwargs['pk']))

    queryset = Room.objects.all()
    serializer_class = ReservationSerializer
