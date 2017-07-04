from django.db import models

class Room(models.Model):
    beds = models.IntegerField()
