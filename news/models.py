from datetime import datetime

from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class Blognews(models.Model):
    Category = models.CharField(max_length=500)
    name = models.CharField(max_length=1000)
    arrival_date = models.CharField(max_length=500)
    Cover_pic = models.ImageField(upload_to='photos')
    Cover_pic1 = models.ImageField(upload_to='photos', blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=100, default=1)
    discreptation = RichTextField(default=1)
    about_writer = RichTextField(default=1)

    def __str__(self):
        return self.name
