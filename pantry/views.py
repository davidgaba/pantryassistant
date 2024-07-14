from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginForm, NewPantryItemForm
from .models import Recipe, PantryItem
from django.db.models import Q
from django.contrib.auth.models import User

# authenticate models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

import requests
import json

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



def fetch_random_recipes(tags):
    url = "https://api.spoonacular.com/recipes/random"

    params = {
        "apiKey": SPOONACULAR_KEY,
        "number": 50,
        "include-tags": tags,
        'limitLicense': 'true',
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:

        # Get recipes
        recipes_data = response.json().get('recipes', [])

        # Filter out recipes without images
        recipes_with_images = [recipe for recipe in recipes_data if recipe.get('image')]

        for recipe_data in recipes_with_images:

            # Start phrase to cut off from spoonacular summary
            cutoff_phrases = ["Similar recipes", "Users who liked this recipe also liked", "If you like this recipe,", "Try <a", "<a"]

            summary = recipe_data['summary']

            for phrase in cutoff_phrases:
                cutoff_index = summary.find(phrase)

                if cutoff_index != -1:
                    summary = summary[:cutoff_index]
                    break

            if recipe_data['spoonacularScore'] > 80:

                Recipe.objects.get_or_create(
                    recipe_id = recipe_data['id'],
                    title = recipe_data['title'].title(),
                    image = recipe_data['image'],
                    summary = summary,
                    source_url = recipe_data['sourceUrl'],
                    dish_types = recipe_data['dishTypes'],
                    servings = recipe_data['servings'],
                    cook_time = recipe_data['readyInMinutes'],
                    instructions = recipe_data['analyzedInstructions'],
                    ingredients = recipe_data['extendedIngredients'],
                    favorite = False,
                )


def fetch_recipes():
    fetch_random_recipes(["main dish"])

    fetch_random_recipes(["snack"])
    fetch_random_recipes(["fingerfood"])
    fetch_random_recipes(["appetizer"])
    fetch_random_recipes(["side dish"])
    
    fetch_random_recipes(["beverage"])
    fetch_random_recipes(["drinks"])
    fetch_random_recipes(["dessert"])


@login_required(login_url='login')
def recipe_list(request):
    
    # fetch_recipes()

    recipes = Recipe.objects.order_by('?')[:10]
    new_recipes = Recipe.objects.order_by('?')[:10]
    mains = Recipe.objects.filter(Q(dish_types__contains='main dish')).order_by('?')[:10]
    snacks = Recipe.objects.filter(Q(dish_types__contains='snack') | Q(dish_types__contains='fingerfood') | Q(dish_types__contains='appetizer') | Q(dish_types__contains='side dish')).order_by('?')[:10]
    beverages = Recipe.objects.filter(Q(dish_types__contains='beverage') | Q(dish_types__contains='drink')).order_by('?')[:10]
    desserts = Recipe.objects.filter(Q(dish_types__contains='dessert')).order_by('?')[:10]

    context = {
        'recipes': recipes,
        'new_recipes': new_recipes,
        'mains' : mains,
        'snacks': snacks,
        'beverages' : beverages,
        'desserts': desserts,
    }
    return render(request, 'pantry/recipe_list.html', context=context)    


@login_required(login_url='login')
def recipe_detail_view(request, id):
    
    recipe = Recipe.objects.get(recipe_id=id)
    steps = recipe.instructions[0].get('steps')

    context = {
        'recipe': recipe,
        'steps' : steps,
    }
    return render(request, 'pantry/recipe_detail.html', context=context)


@login_required(login_url='login')
def pantry_list(request):

    if request.method == 'POST':
        new_item_form = NewPantryItemForm(request.POST)

        if new_item_form.is_valid():
            new_item = new_item_form.save(commit=False)
            new_item.user = request.user  # Set the user before saving
            new_item.save()
            return redirect('pantry_list')  # Redirect to the same view after saving
        elif request.POST.get("save"):
            
            return redirect('pantry_list')
    else:
        new_item_form = NewPantryItemForm()

    pantry_items = PantryItem.objects.filter(user=request.user)

    context = {
        'new_item_form' : NewPantryItemForm(),
        'pantry_items': pantry_items, 
    }

    return render(request, 'pantry/pantry.html', context=context)


@login_required(login_url='login')
def grocery_list(request):
    return render(request, 'pantry/grocery_list.html')

