from django.urls import path

from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('recipes/list/', RecipeListView.as_view(), name="recipelist"),
    path('recipe/<int:id>/', RecipeDetailView.as_view(), name="recipedetail"),
]
# This might be needed, depending on your Django version
app_name = "ledger"