from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),    
    path("annonce/",views.annonce,name="annonce"),
    path("annonceinfos/",views.annonceinfos,name="annonceinfos"),
]
