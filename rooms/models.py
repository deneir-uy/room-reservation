from django.db import models

class Room(models.Model):
    beds = models.IntegerField()

    def __str__(self):
        return "{}: {}".format(self.id, self.beds)
