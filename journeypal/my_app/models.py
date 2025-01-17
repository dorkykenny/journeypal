from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    description = models.TextField()
    user =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('city-detail', kwargs={'city_id': self.id})
    

class Attraction(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta: 
        ordering = ['name']

class BucketList(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cities = models.ManyToManyField(City, related_name='bucket_lists')
    
    def __str__(self):
        return f"{self.name} - {self.user.username}'s Bucket List"
    
    def get_absolute_url(self):
        return reverse('bucketlist-detail', kwargs={'bucketlist_id': self.id})

    class Meta:
        verbose_name = "Bucket List"
        verbose_name_plural = "Bucket Lists"