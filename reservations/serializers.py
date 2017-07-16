from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.ReadOnlyField(source='pk'))
    room = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.ReadOnlyField(source='pk'))

    class Meta:
        model = Reservation
        fields = ('room', 'user')
