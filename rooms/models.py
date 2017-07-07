from django.db import models


class Room(models.Model):
    beds = models.IntegerField()
    room_number = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return "{}: {}".format(self.id, self.room_number)


class User(models.Model):
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {}".format(self.room.id, self.room.room_number)
