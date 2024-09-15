from django.db import models


class APIRequestLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=200)
    query_params = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    remote_addr = models.CharField(max_length=15)
    user_agent = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.timestamp} - {self.method} {self.path}"
