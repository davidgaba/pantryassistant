from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

# Create your models here.

class Recipe(models.Model):
    recipe_id = models.IntegerField()
    title = models.CharField(max_length=255, default='')
    image = models.URLField(default='')
    summary = models.TextField(default='')
    source_url = models.URLField(default='')
    dish_types = models.TextField(default='')
    servings = models.IntegerField(default=1)
    cook_time = models.IntegerField(default=0)
    instructions = JSONField(default='')
    ingredients = JSONField(default='')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class PantryItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    in_stock = models.BooleanField(default=True)
    quantity = models.IntegerField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.quantity}"