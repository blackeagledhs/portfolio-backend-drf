from django.db import models


class Other(models.Model):
    institute = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    year = models.IntegerField()
    image = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.title