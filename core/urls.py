from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),    
    path("annonce/",views.annonce,name="annonce"),
    path("searchNote/",views.SearchNote,name="SearchNote"),
    path("homeProf/", views.homeProf, name="homeProf"),
    path("chatbot/", views.chatbot, name="chatbot"),
    path("addanounce/", views.addAnounce, name="addAnounce"),
    path("ecours/", views.ecours, name="ecours"),
    
]
