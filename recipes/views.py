from django.shortcuts import render

from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")
    return render(
        request,
        "recipes/pages/home.html",
        context={
            "recipes": recipes,
        },
    )


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id).order_by("-id")
    return render(
        request,
        "recipes/pages/category.html",
        context={
            "recipes": recipes,
            "category_name": recipes.first().category.name,
        },
    )


def recipe(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id, is_published=True).first()
    return render(
        request,
        "recipes/pages/recipe-view.html",
        context={
            "recipe": recipe,
            "is_detail_page": True,
        },
    )
