from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gestionNotes/", views.gestionNotes, name="gestionNotes"),
]
