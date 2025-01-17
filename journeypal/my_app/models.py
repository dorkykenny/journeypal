from django.db import models
from django.urls import reverse

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('city-detail', kwargs={'city_id': self.id})