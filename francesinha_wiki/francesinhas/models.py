from django.db import models
from django.urls import reverse


class Ingredients(models.Model):
    name = models.CharField(max_length=512, unique=True)
    
    def __str__(self):
        return self.name
    
    
class Francesinha(models.Model):
    name = models.CharField(max_length=512, unique=True)
    price = models.BigIntegerField()
    rating = models.DecimalField(max_digits=4, decimal_places=1)
    ingredients = models.ManyToManyField(Ingredients, related_name='ingredients')  # Relacionamento muitos-para-muitos
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("francesinha-view", kwargs={"id": self.id})
