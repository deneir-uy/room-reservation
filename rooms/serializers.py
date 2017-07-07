from rest_framework import serializers
from .models import Room, Reservation, User


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=User.objects.get(pk=1))
    room = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.ReadOnlyField(source='pk'))

    class Meta:
        model = Reservation
        fields = '__all__'
