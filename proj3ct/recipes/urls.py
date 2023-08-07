from django.urls import path

from . import views


urlpatterns = [
    path("", views.home),
    path("recipes/<int:_id>/", views.recipe),
]
