from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

# authenticate models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Recipe

import requests

from dotenv import load_dotenv
import os

load_dotenv()
SPOONACULAR_KEY = os.environ.get('SPOONACULAR_KEY')


# Create your views here.
def home(request):
    return render(request, 'pantry/index.html')


def register(request):
    
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {'register_form': form}

    return render(request, 'pantry/register.html', context=context)


def login(request):

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('recipe_list')

    context = {'login_form': form}

    return render(request, 'pantry/login.html', context=context)


def logout(request):

    auth.logout(request)

    return redirect("login")


def fetch_random_recipes():
    url = "https://api.spoonacular.com/recipes/random"

    params = {
        "apiKey": SPOONACULAR_KEY,
        "number": 1
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        recipes_data = response.json().get('recipes', [])

        for recipe_data in recipes_data:

            Recipe.objects.get_or_create(
                recipe_id = recipe_data['id'],
                title = recipe_data['title'],
                image = recipe_data['image'],
                summary = recipe_data['summary'],
                source_url = recipe_data['sourceUrl']
            )


@login_required(login_url='login')
def recipe_list(request):
    # fetch_random_recipes()
    recipes = Recipe.objects.order_by('?')[:7]
    context = {
        'recipes': recipes
    }
    return render(request, 'pantry/recipe_list.html', context=context)    

@login_required(login_url='login')
def pantry_list(request):
    return render(request, 'pantry/pantry.html')

@login_required(login_url='login')
def grocery_list(request):
    return render(request, 'pantry/grocery_list.html')

