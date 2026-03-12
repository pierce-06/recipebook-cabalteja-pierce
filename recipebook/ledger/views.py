from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.decorators import login_required

from .forms import RecipeForm, RecipeImageForm


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/recipelist.html', {'recipes': recipes})


@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'recipe/recipedetail.html', {'recipe': recipe})

@login_required
def recipe_add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user.profile
            recipe.save()
            return redirect('../../recipes/list')
    else:
        form = RecipeForm()
    return render(request, 'recipe/recipeadd.html', {'form': form})
        
@login_required
def recipe_add_image(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeImageForm()

    return render(request, 'recipe/recipeaddimage.html', {'form': form, 'recipe': recipe})