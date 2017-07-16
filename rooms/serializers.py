from rest_framework import serializers
from .models import Room, Reservation
from django.contrib.auth.models import User


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('beds', 'price')


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.ReadOnlyField(source='pk'))
    room = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.ReadOnlyField(source='pk'))

    class Meta:
        model = Reservation
        fields = ('room', 'user')
