from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Restaurant
from .forms import RestaurantForm


# view to update a restaurant
def restaurant_update_view(request, id):
    obj = get_object_or_404(Restaurant, id = id)
    form = RestaurantForm(instance = obj)
    if request.method == "POST":
        form = RestaurantForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('../')
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "restaurants/restaurant_update.html", context)


# viw to list restaurants
def restaurant_all_view(request):

    obj = Restaurant.objects.all()
    context = {
        "objects": obj
    }
    return render(request, "restaurants/restaurant.html", context)


# view to show a restaurant
def restaurant_detail_view(request, id):
    try:
        obj = get_object_or_404(Restaurant, id = id)
    except Restaurant.DoesNotExist:
        raise Http404
    context = {
        "objects": obj
    }

    return render(request, "restaurants/restaurant_individual.html", context)


# view to delete a restaurant
def restaurant_delete_view(request, id):
    
    obj = get_object_or_404(Restaurant, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }

    return render(request, "restaurants/restaurant_delete.html", context)


# view to create a francesinha
def restaurant_create_view(request):
    form = RestaurantForm()
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m() 
            form = RestaurantForm()
        else:
            print(form.errors)
               
    context = {
        "form": form
    }
    return render(request, "restaurants/restaurant_create.html", context)



def restaurant_list_view(request):
    query = request.GET.get('q')
    
    if query:
        objs = Restaurant.objects.filter(name__icontains=query)
    else:
        objs = Restaurant.objects.all()

    context = {
        "objects": objs
    }
    return render(request, "restaurants/restaurant_list.html", context)