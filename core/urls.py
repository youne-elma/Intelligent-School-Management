from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("annonce/",views.annonce,name="annonce"),
    path("SearchNote/",views.SearchNote,name="SearchNote"),

   

]
