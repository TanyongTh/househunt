from django.db import models
from django.utils import timezone


# Create your models here.

class Property(models.Model):
    property_id = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    suburb_name = models.CharField(max_length=200, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    listed_date = models.DateTimeField(null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    sold_date = models.DateTimeField(null=True, blank=True)
    sold_price = models.CharField(max_length=200, null=True, blank=True)
    listed_agent = models.CharField(max_length=200, null=True, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    modify_date = models.DateTimeField(default=timezone.now)

