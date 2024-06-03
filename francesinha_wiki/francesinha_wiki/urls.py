"""
URL configuration for francesinha_wiki project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from francesinhas.views import (home_view, 
                                francesinha_all_view, 
                                francesinha_create_view, 
                                francesinha_detail_view,
                                francesinha_delete_view,
                                francesinha_update_view,
                                ingredient_all_view,
                                ingredient_detail_view,
                                ingredient_update_view,
                                ingredient_delete_view,
                                ingredient_create_view,
                                search_view,
                                )

from restaurants.views import (restaurant_all_view,
                               restaurant_detail_view,
                               restaurant_update_view,
                               restaurant_create_view,
                               restaurant_delete_view,
                               )


urlpatterns = [

    path('admin/', admin.site.urls),
    path('francesinha/', francesinha_all_view, name='francesinha'),
    path('francesinha/create/', francesinha_create_view, name='francesinha-create'),
    path('francesinha/<int:id>/', francesinha_detail_view, name='francesinha-view'),
    path('francesinha/<int:id>/delete/', francesinha_delete_view, name='francesinha-remove'),
    path('francesinha/<int:id>/update/', francesinha_update_view, name='francesinha-update'),
    path('restaurant/', restaurant_all_view, name='restaurant'),
    path('restaurant/create/', restaurant_create_view, name='restaurant-create'),
    path('restaurant/<int:id>/', restaurant_detail_view, name='restaurant-view'),
    path('restaurant/<int:id>/update/', restaurant_update_view, name='restaurant-update'),
    path('restaurant/<int:id>/delete/', restaurant_delete_view, name='restaurant-remove'),
    path('ingredients/', ingredient_all_view, name='ingredient'),
    path('ingredients/create', ingredient_create_view, name='ingredient-create'),
    path('ingredients/<int:id>', ingredient_detail_view, name='ingredient-view'),
    path('ingredients/<int:id>/update/', ingredient_update_view, name='ingredient-update'),
    path('ingredients/<int:id>/delete/', ingredient_delete_view, name='ingredient-remove'),
    path('search/', search_view, name='search'),
    path('', home_view, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
