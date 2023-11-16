from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import SightingForm
from .models import Finch, Food

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    food_list = finch.foods.all().values_list('id')
    not_food_list = Food.objects.exclude(id__in=food_list)
    sighting_form = SightingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch,
        'sighting_form': sighting_form,
        'foods': not_food_list
    })

def add_sighting(request, finch_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.finch_id = finch_id
        new_sighting.save()
    return redirect('detail', finch_id=finch_id) 

def assoc_food(request, finch_id, food_id):
    Finch.objects.get(id=finch_id).foods.add(food_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_food(request, finch_id, food_id):
    Finch.objects.get(id=finch_id).foods.remove(food_id)
    return redirect('detail', finch_id=finch_id)

class FoodCreate(CreateView):
    model = Food
    fields = ['name']

class FinchCreate(CreateView):
    model = Finch
    fields = ['type', 'appearance', 'seen', 'image']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'type', 'appearance', 'seen', 'image']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'