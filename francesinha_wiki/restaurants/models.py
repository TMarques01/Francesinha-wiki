from django.db import models
from django.urls import reverse
from django.contrib import admin
from francesinhas.models import Francesinha
from francesinhas.models import SoftDeleteManager

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=512, unique=True)
    address = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    country = models.CharField(max_length=512)
    rating = models.DecimalField(max_digits=4, decimal_places=1)
    francesinhas = models.ManyToManyField(Francesinha, related_name='restaurants')  # Relacionamento muitos-para-muitos
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("restaurant-view", kwargs={"id": self.id})


# Class to show all Restaurants in the admin panel
class RestaurantAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return self.model.all_objects.all()