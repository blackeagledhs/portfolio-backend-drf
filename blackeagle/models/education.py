from django.db import models

class Education(models.Model):
    institute = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    desccription = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title