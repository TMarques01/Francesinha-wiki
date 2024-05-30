from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Francesinha, Ingredients
from .forms import FrancesinhaForm


# Create your views here.
def home_view(request):
    return render(request, "home.html", {})


# view to update a francesinha
def francesinha_update_view(request, id):
    obj = get_object_or_404(Francesinha, id = id)
    form = FrancesinhaForm(instance = obj)
    if request.method == "POST":
        form = FrancesinhaForm(request.POST, instance = obj)
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


# view to create a francesinha
def francesinha_create_view(request):
    form = FrancesinhaForm()
    if request.method == "POST":
        form = FrancesinhaForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m() 
            form = FrancesinhaForm()
        else:
            print(form.errors)
               
    context = {
        "form": form
    }
    return render(request, "francesinha/francesinha_create.html", context)


# view to search for francesinhas
def francesinha_list_view(request):
    query = request.GET.get('q')
    if query:
        objs = Francesinha.objects.filter(name__icontains=query)
    else:
        objs = Francesinha.objects.all()

    context = {
        "objects": objs
    }
    return render(request, "francesinha/francesinha_list.html", context)