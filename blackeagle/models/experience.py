from django.db import models


class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    month_of_income = models.CharField(max_length=10)
    year_of_income = models.IntegerField()
    month_of_egress = models.CharField(max_length=10)
    year_of_egress = models.IntegerField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.position
