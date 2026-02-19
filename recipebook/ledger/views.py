from django.shortcuts import render
from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/recipelist.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'recipe/recipedetail.html', {'recipe': recipe})
