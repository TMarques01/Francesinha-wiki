from django.contrib import admin

# Register your models here.
from .models import Francesinha, Ingredients

admin.site.register(Francesinha)
admin.site.register(Ingredients)
