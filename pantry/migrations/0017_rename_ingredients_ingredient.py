# Generated by Django 5.0.6 on 2024-07-26 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0016_ingredients_recipe_cuisines'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
    ]
