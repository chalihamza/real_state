from datetime import datetime

from ckeditor.fields import RichTextField
from django.db import models

from multiselectfield import MultiSelectField


# Create your models here.
from pages.models import Agent


class House_property(models.Model):
    state_choice = (
        ('PU', 'punjab'),
        ('KPK', 'khyber pukhtankhwa'),
        ('BL', 'blochistan'),
        ('FD', 'fedral Territory'),
        ('SN', 'sindh'),
        ('KS', 'kashmir'),
    )
    Property_type_choice = (
        ('house', 'house'),
        ('shop', 'shop'),
    )
    Status_choice = (
        ('sale', 'sale'),
        ('Rent', 'Rent'),
    )
    Amenities_choice = (
        ('Balcony', 'Balcony'),
        ('Deck', 'Deck'),
        ('Parking', 'Parking'),
        ('Outdoor Kitchen', 'Outdoor Kitchen'),
        ('Tennis Courts', 'Tennis Courts'),
        ('Sun Room', 'Sun Room'),
        ('Cable Tv', 'Cable Tv'),
        ('Internet', 'Internet'),
        ('Garden', 'Garden'),
        ('Concrete Flooring', 'Concrete Flooring')
    )
    address = models.CharField(max_length=1000)
    house_no = models.CharField(max_length=400)
    Property_ID = models.IntegerField()
    # Location = models.CharField(max_length=500, null=True)
    Property_Type = models.CharField(choices=Property_type_choice, max_length=300)
    Amenities = MultiSelectField(choices=Amenities_choice)
    image = models.ImageField(upload_to='photos')
    image1 = models.ImageField(upload_to='photos', blank=True)
    image2 = models.ImageField(upload_to='photos', blank=True)
    image3 = models.ImageField(upload_to='photos', blank=True)
    image4 = models.ImageField(upload_to='photos', blank=True)
    image5 = models.ImageField(upload_to='photos', blank=True)
    state = models.CharField(choices=state_choice, max_length=300)
    Ubication = models.URLField(max_length=5000, default=1)
    video = models.URLField(max_length=50000, default=1)
    city = models.CharField(max_length=200)
    condition = models.CharField(max_length=100)
    Description = RichTextField()
    price = models.CharField(max_length=500)
    Status = models.CharField(choices=Status_choice, max_length=5000)
    Area = models.CharField(max_length=500)
    BedsRoom = models.IntegerField()
    Bath = models.IntegerField()
    Garages = models.IntegerField()
    no_of_owners = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, null=True, blank=True)

    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    # name = models.CharField(max_length=50)
    # contact_no = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.address

