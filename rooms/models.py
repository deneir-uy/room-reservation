from django.db import models


class Room(models.Model):
    beds = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return "{}".format(self.id)
