from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField()

class Recipe(models.Model):
    name = models.CharField()

class RecipeIngredient(models.Model):
    quantity = models.CharField()
    ingredient = models.ForeignKey(Ingredient, 
                                   on_delete=models.CASCADE, 
                                   related_name="recipe")
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE, 
                               related_name="ingredient")
    
    def ingredient_str(self):
        return self.ingredient
    def recipe_str(self):
        return self.recipe
    def ingredient_absolute_url(self):
        return reverse('ingredient_name', args=[str(self.ingredient)])
    def recipe_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.recipe)])
# Create your models here.
