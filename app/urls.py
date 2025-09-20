from django.urls import path
from .views import (
    Main,
    ChefListView,
    ChefCreateView,
    ChefDetailView,
    ChefDeleteView,
    ChefUpdateView,
    CategoryListView,
    CategoryCreateView,
    CategoryDeleteView,
    RecipeListView,
    RecipeCreateView,
    RecipeDeleteView,
    RecipeDetailView,
    RecipeUpdateView,
)

urlpatterns = [
    path('main/', Main.as_view(), name='main'),


    path('chefs/', ChefListView.as_view(), name='chefs'),
    path('chef_add/', ChefCreateView.as_view(), name='chef_add'),
    path('chef_info/<int:pk>/', ChefDetailView.as_view(), name='chef_info'),
    path('chef_update/<int:pk>/', ChefUpdateView.as_view(), name='chef_update'),
    path('chef_delete/<int:pk>/', ChefDeleteView.as_view(), name='chef_delete'),

    
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category_add/', CategoryCreateView.as_view(), name='category_add'),
    path('category_delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),


    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('recipe_add/', RecipeCreateView.as_view(), name='recipe_add'),
    path('recipe_info/<int:pk>/', RecipeDetailView.as_view(), name='recipe_info'),
    path('recipe_update/<int:pk>/', RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipe_delete/<int:pk>/', RecipeDeleteView.as_view(), name='recipe_delete'),
]
