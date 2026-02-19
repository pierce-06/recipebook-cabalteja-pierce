from django.shortcuts import render
from .models import RecipeIngredient

def recipe_list(request):
    rcp = {
        "recipes": [
            {
                "name": "Recipe 1",
                "ingredients": [
                    {
                        "name": "tomato",
                        "quantity": "3pcs"
                    },
                    {
                        "name": "onion",
                        "quantity": "1pc"
                    },
                    {
                        "name": "pork",
                        "quantity": "1kg"
                    },
                    {
                        "name": "water",
                        "quantity": "1L"
                    },
                    {
                        "name": "sinigang mix",
                        "quantity": "1 packet"
                    }
                ],
                "link": "/recipe/1/"
            },
            {
                "name": "Recipe 2",
                "ingredients": [
                    {
                        "name": "garlic",
                        "quantity": "1 head"
                    },
                    {
                        "name": "onion",
                        "quantity": "1pc"
                    },
                    {
                        "name": "vinegar",
                        "quantity": "1/2cup"
                    },
                    {
                        "name": "water",
                        "quantity": "1 cup"
                    },
                    {
                        "name": "salt",
                        "quantity": "1 tablespoon"
                    },
                    {
                        "name": "whole black peppers",
                        "quantity": "1 tablespoon"
                    },
                    {
                        "name": "pork",
                        "quantity": "1 kilo"
                    }
                ],
                "link": "/recipe/2/"
            }
        ]
    }
    return render(request, "recipe/recipelist.html", rcp)

def recipe_list_view(request):
    recipes = Rec
    return render(request, "recipe/recipelist.html", rlv)

def first_recipe(request):
    first_recipe_dict = {
        "name": "Recipe 1",
        "ingredients": [
            {
                "name": "tomato",
                "quantity": "3 pcs"
            },
            {
                "name": "onion",
                "quantity": "1 pc"
            },
            {
                "name": "pork",
                "quantity": "1 kg"
            },
            {
                "name": "water",
                "quantity": "1 L"
            },
            {
                "name": "sinigang mix",
                "quantity": "1 packet"
            }
        ],
        "link": "/recipe/1"
    }
    return render(request, "recipe/firstrecipe.html", first_recipe_dict)

def second_recipe(request):
    second_recipe_dict = {
        "name": "Recipe 2",
        "ingredients": [
            {
                "name": "garlic",
                "quantity": "1 head"
            },
            {
                "name": "onion",
                "quantity": "1 pc"
            },
            {
                "name": "vinegar",
                "quantity": "1/2 cup"
            },
            {
                "name": "water",
                "quantity": "1 cup"
            },
            {
                "name": "salt",
                "quantity": "1 tablespoon"
            },
            {
                "name": "whole black peppers",
                "quantity": "1 tablespoon"
            },
            {
                "name": "pork",
                "quantity": "1 kilo"
            }
        ],
        "link": "/recipe/2"
    }
    return render(request, "recipe/secondrecipe.html", second_recipe_dict)
