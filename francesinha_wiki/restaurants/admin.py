from django.contrib import admin

# Register your models here.
from .models import Restaurant, RestaurantAdmin

admin.site.register(Restaurant, RestaurantAdmin)
