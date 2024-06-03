from django.db import models
from django.urls import reverse
from django.contrib import admin


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super(SoftDeleteManager, self).get_queryset().filter(is_deleted=False)
  
  
# General class for Ingredients
class Ingredients(models.Model):
    name = models.CharField(max_length=512, unique=True)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()
    all_objects = models.Manager()
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse("ingredient-view", kwargs={"id": self.id})
  
  
# General class for Francesinhas
class Francesinha(models.Model):
    name = models.CharField(max_length=512, unique=True)
    price = models.BigIntegerField()
    rating = models.DecimalField(max_digits=4, decimal_places=1)
    ingredients = models.ManyToManyField(Ingredients, related_name='ingredient')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    
    objects = SoftDeleteManager()
    all_objects = models.Manager()
    
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()


    def hard_delete(self, *args, **kwargs):
        super(Francesinha, self).delete(*args, **kwargs)
    
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse("francesinha-view", kwargs={"id": self.id})
    

# Class to show all Francesinhas in the admin panel
class FrancesinhaAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return self.model.all_objects.all()


# Class to show all Ingredients in the admin panel
class IngredientAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return self.model.all_objects.all()