from django.db import models
from jsonfield import JSONField

# Create your models here.

class Recipe(models.Model):
    recipe_id = models.IntegerField()
    title = models.CharField(max_length=255)
    image = models.URLField(default='')
    summary = models.TextField(default='')
    source_url = models.URLField(default='')
    dish_types = models.TextField(default=[])
    ingredients = JSONField()
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title