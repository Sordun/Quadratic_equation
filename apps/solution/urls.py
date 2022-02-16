from django.urls import path

from . import views


urlpatterns = [
    path("", views.calculator, name="calculator"),
    path("1/", views.guess_the_color, name="guess_the_color"),
]
