from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_id = models.IntegerField()
    title = models.CharField(max_length=255)
    image = models.URLField()
    summary = models.TextField()
    source_url = models.URLField()

    def __str__(self):
        return self.title