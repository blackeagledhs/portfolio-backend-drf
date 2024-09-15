from django.db import models


class Badge(models.Model):
    badge = models.CharField(max_length=255, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

