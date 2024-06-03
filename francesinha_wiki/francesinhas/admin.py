from django.contrib import admin

# Register your models here.
from .models import Francesinha, Ingredients, FrancesinhaAdmin, IngredientAdmin

admin.site.register(Francesinha, FrancesinhaAdmin)
admin.site.register(Ingredients, IngredientAdmin)
