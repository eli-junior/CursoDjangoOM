from django.shortcuts import render

from recipes.utils.factory import make_recipe


def home(request):
    return render(
        request,
        "recipes/pages/home.html",
        context={
            "recipes": make_recipe(12),
        },
    )


def recipe(request, id):
    return render(
        request,
        "recipes/pages/recipe-view.html",
        context={
            "recipe": make_recipe(),
        },
    )
