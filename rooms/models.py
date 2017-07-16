from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    beds = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return "{}".format(self.id)


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.room.id)
