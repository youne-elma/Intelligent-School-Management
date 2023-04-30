from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gestionnotesmenuadmin/", views.gestionnotesmenuadmin, name="gestionnotesmenuadmin"),

]
