from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/recipelist.html', {'recipes': recipes})

@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'recipe/recipedetail.html', {'recipe': recipe})
