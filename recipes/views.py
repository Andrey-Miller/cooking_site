from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe, Category
from .forms import RecipeForm


def index(request):
    categories = Category.objects.all()
    recipes = Recipe.objects.order_by('?')[:6]
    return render(request, 'main_page/index.html', {'categories': categories, 'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


def category_recipes(request, category_id):
    recipes = Recipe.objects.filter(category_id=category_id)
    per_page = 6
    paginator = Paginator(recipes, per_page)
    page_number = request.GET.get('page')
    try:
        recipes_paginator = paginator.page(page_number)
    except PageNotAnInteger:
        recipes_paginator = paginator.page(1)
    except EmptyPage:
        recipes_paginator = paginator.page(paginator.num_pages)
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes_paginator})


def recipe_list(request):
    recipes = Recipe.objects.order_by('id')
    per_page = 6
    paginator = Paginator(recipes, per_page)
    page_number = request.GET.get('page')
    try:
        recipes_paginator = paginator.page(page_number)
    except PageNotAnInteger:
        recipes_paginator = paginator.page(1)
    except EmptyPage:
        recipes_paginator = paginator.page(paginator.num_pages)
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes_paginator})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'recipes/category_list.html', {'categories': categories})


def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'recipes/category_list.html', {'category': category})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            category = form.cleaned_data['category']
            recipe.category = category
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html',
                  {'form': form})


@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            category = form.cleaned_data['category']
            recipe.category = category
            recipe.save()
            return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/edit_recipe.html',
                  {'form': form, 'recipe': recipe})
