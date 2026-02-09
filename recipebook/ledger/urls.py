from django.urls import path

from .views import recipe_list, first_recipe, second_recipe

urlpatterns = [
    path('recipes/list/', recipe_list, name="recipelist"),
    path('recipe/1/', first_recipe, name="firstrecipe"),
    path('recipe/2/', second_recipe, name="secondrecipe")
]
# This might be needed, depending on your Django version
app_name = "ledger"