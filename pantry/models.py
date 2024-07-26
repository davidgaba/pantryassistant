from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

# Create your models here.

class Ingredient(models.Model):
    ingredient_id = models.IntegerField()
    name = models.CharField(max_length=255, default='')
    substitutes = JSONField(default='')

    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    recipe_id = models.IntegerField()
    title = models.CharField(max_length=255, default='')
    image = models.URLField(default='')
    summary = models.TextField(default='')
    source_url = models.URLField(default='')
    cuisines = models.TextField(default='')
    dish_types = models.TextField(default='')
    servings = models.IntegerField(default=1)
    cook_time = models.IntegerField(default=0)
    instructions = JSONField(default='')
    ingredients = JSONField(default='')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class PantryItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    in_stock = models.BooleanField(default=True)
    quantity = models.IntegerField(default='', blank=True, null=True)
    units = models.CharField(max_length=50, default="", blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"({self.user}):\n\t{self.name.title()} - {self.id}\n\tIn stock: {self.in_stock}\n\tQuantity: {self.quantity}\n\tUnits: {self.units}\n\tExpiration Date: {self.expiration_date}"
 