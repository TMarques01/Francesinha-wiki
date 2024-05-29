from django.db import models
from francesinhas.models import Francesinha
from django.urls import reverse

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=512, unique=True)
    address = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    country = models.CharField(max_length=512)
    rating = models.DecimalField(max_digits=4, decimal_places=1)
    francesinhas = models.ManyToManyField(Francesinha, related_name='restaurants')  # Relacionamento muitos-para-muitos

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("restaurant-view", kwargs={"id": self.id})
