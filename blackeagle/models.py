from django.db import models


class Education(models.Model):
    institute = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    desccription = models.TextField(blank=True, null=True)
    image = models.URLField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


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


class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    project_url = models.URLField()
    image = models.URLField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name


class About(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    selfie = models.URLField(null=False)
    position = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name