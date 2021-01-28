from django.db import models


class Role(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    experience = models.PositiveSmallIntegerField()
    salary = models.CharField(max_length=50, blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    responsibility = models.TextField(blank=True, null=True)
    others = models.TextField(blank=True, null=True)
    publish = models.BooleanField(default=False)
