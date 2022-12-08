from datetime import datetime

from django.db import models

from ckeditor.fields import RichTextField


# Create your models here.
class Agent(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/%Y/%M/%d/')
    facebook = models.URLField(max_length=200)
    google = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    date = models.DateTimeField(default=datetime.now, blank=True)
    email = models.EmailField()
    contact_no = models.IntegerField()

    def __str__(self):
        return self.FirstName


class Testimonial(models.Model):
    Name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos')
    image1 = models.ImageField(upload_to='photos')
    discreptation = RichTextField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.Name
