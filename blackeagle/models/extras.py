from django.db import models


class Extras(models.Model):
    activity = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return self.activity
