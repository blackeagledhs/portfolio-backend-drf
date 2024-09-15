from django.db import models


class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    project_url = models.URLField()
    image = models.CharField(max_length=255, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name
