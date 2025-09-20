from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Chef, Recipe, Category, Main

class ChefListView(ListView):
    model = Chef
    fields = ['full_name','mutaxassislik', 'tajriba']
    template_name = 'chef_list.html'
    context_object_name = "chef_list"

class ChefCreateView(CreateView):
    model = Chef
    fields = ['full_name', 'mutaxassislik', 'tajriba', 'bio', 'email','telefon']  
    template_name = 'chef_add.html'
    success_url = reverse_lazy('chefs')   

class ChefDetailView(DetailView):
    model = Chef
    template_name = 'chef_detail.html'  
    context_object_name = "chef" 

class ChefUpdateView(UpdateView):
    model = Chef
    fields = ['full_name', 'mutaxassislik', 'tajriba', 'bio', 'email','telefon'] 
    template_name = 'chef_update.html'
    success_url = reverse_lazy('chefs')

class ChefDeleteView(DeleteView):
    model = Chef
    template_name = 'chef_delete.html'
    success_url = reverse_lazy('chefs')

    



class RecipeListView(ListView):
    model = Recipe
    fields = ['nomi', 'tavsif', 'ingredientlar', 'kategoriya', 'chef', 'yaratilgan']
    template_name = 'recipe_list.html'
    context_object_name = "recipe_list"

class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['nomi', 'tavsif', 'ingredientlar', 'kategoriya', 'chef']
    template_name = "recipe_add.html"
    success_url = '/recipes/'   

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'   

class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['nomi', 'tavsif', 'ingredientlar', 'kategoriya', 'chef']
    template_name = 'recipe_update.html'
    success_url = reverse_lazy('recipes')

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('recipes')
    




class CategoryListView(ListView):
    model = Category
    fields = ['kategoriya', 'tavsif']
    template_name = 'category_list.html'
    context_object_name = "categories"

class CategoryCreateView(CreateView):
    model = Category
    fields = ['kategoriya', 'tavsif']
    template_name = 'category_add.html'
    success_url = reverse_lazy('categories')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('categories')

class Main(ListView):
    model = Main
    template_name = 'main.html'
# Create your views here.
