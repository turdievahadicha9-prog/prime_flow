from django.db import models


class About(models.Model):
    company_name = models.CharField(max_length=100, default="Prime Flow")
    slogan = models.CharField(max_length=200)
    description = models.TextField()

    history = models.TextField()
    founded_year = models.IntegerField()

    mission = models.TextField()
    values = models.TextField()

    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    working_hours = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Advantage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.title