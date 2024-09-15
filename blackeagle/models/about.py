from django.db import models


class About(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    selfie = models.CharField(max_length=255, null=True)
    position = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
