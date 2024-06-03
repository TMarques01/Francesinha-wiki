from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Francesinha, Ingredients
from .forms import FrancesinhaForm, IngredientsForm
from restaurants.models import Restaurant

# Auxiliar function to get objects and order them
def get_objects_and_order(model, query, order_type):
    if query and query.strip() != '':
        objects = model.objects.filter(name__icontains=query)
    else:
        objects = model.objects.all()

    if order_type == 'rating':
        return objects.order_by('-rating')
    elif order_type == 'name':
        return objects.order_by('name')
    else:
        return objects


# Create your views here.
def home_view(request):
    return render(request, "home.html", {})


# view for the general search
def search_view(request):
    query = request.GET.get('q')
    search_type = request.GET.get('type')
    order_type = request.GET.get('order')
    
    francesinhas = []
    restaurants = []
    ingredients = []
    
    if search_type and order_type:
        if search_type == 'francesinha':
            francesinhas = get_objects_and_order(Francesinha, query, order_type)
        elif search_type == 'restaurant':
            restaurants = get_objects_and_order(Restaurant, query, order_type)
        elif search_type == 'ingredient':
            if order_type != 'rating':
                ingredients = get_objects_and_order(Ingredients, query, order_type)
        

    context = {
        "francesinhas": francesinhas,
        "restaurants": restaurants,
        "ingredients": ingredients,
    }
    return render(request, "search.html", context)


#======================== Francesinha Views =================================================


# view to update a francesinha
def francesinha_update_view(request, id):
    obj = get_object_or_404(Francesinha, id = id)
    form = FrancesinhaForm(instance = obj)
    if request.method == "POST":
        form = FrancesinhaForm(request.POST, request.FILES, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('../../')
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "francesinha/francesinha_update.html", context)


# viw to list francesinhas (individual or all)
def francesinha_all_view(request):

    obj = Francesinha.objects.all()
    context = {
        "objects": obj
    }
    return render(request, "francesinha/francesinha.html", context)


# view to show an individual francesinha
def francesinha_detail_view(request, id):
    try:
        obj = get_object_or_404(Francesinha, id = id)
    except Francesinha.DoesNotExist:
        raise Http404
    context = {
        "objects": obj
    }

    return render(request, "francesinha/francesinha_individual.html", context)


# view to create a francesinha
def francesinha_create_view(request):
    form = FrancesinhaForm()
    if request.method == "POST":
        form = FrancesinhaForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m() 
            form = FrancesinhaForm()
            return redirect('../')
        else:
            print(form.errors)
               
    context = {
        "form": form
    }
    return render(request, "francesinha/francesinha_create.html", context)


# view to delete a francesinha
def francesinha_delete_view(request, id):
    
    obj = get_object_or_404(Francesinha, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }

    return render(request, "francesinha/francesinha_delete.html", context)


#======================== Ingredients Views =================================================


# view to show all ingredients
def ingredient_all_view(request):

    obj = Ingredients.objects.all()
    context = {
        "objects": obj
    }
    return render(request, "ingredients/ingredients.html", context)


# view to show an individual ingredient
def ingredient_detail_view(request, id):
    try:
        obj = get_object_or_404(Ingredients, id = id)
    except Ingredients.DoesNotExist:
        raise Http404
    context = {
        "objects": obj
    }

    return render(request, "ingredients/ingredients_individual.html", context)


# view to update a ingredient
def ingredient_update_view(request, id):
    obj = get_object_or_404(Ingredients, id = id)
    form = IngredientsForm(instance = obj)
    if request.method == "POST":
        form = IngredientsForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('../../')
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "ingredients/ingredients_update.html", context)


# view to delete a ingredient   
def ingredient_delete_view(request, id):
    
    obj = get_object_or_404(Ingredients, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }

    return render(request, "ingredients/ingredients_delete.html", context)


# view to create a francesinha
def ingredient_create_view(request):
    form = IngredientsForm()
    if request.method == "POST":
        form = IngredientsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form = IngredientsForm()
            redirect('../')
        else:
            print(form.errors)
               
    context = {
        "form": form
    }
    return render(request, "ingredients/ingredients_create.html", context)