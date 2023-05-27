from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),    
    path("annonce/",views.annonce,name="annonce"),
    path("searchNote/",views.searchNote,name="searchNote"),
    path("homeProf/", views.homeProf, name="homeProf"),
    path("chatbot/", views.chatbot, name="chatbot"),
    path("addanounce/", views.addAnounce, name="addAnounce"),
    path("correctionNote/", views.correctionNote, name="correctionNote"),
    path("ecours/", views.ecours, name="ecours"),
    path("annonceinfos/", views.annonceinfos, name="annonceinfos"),
    path("sessionRattrapage/", views.sessionRattrapage, name="sessionRattrapage"),
    path("sessionNormale/", views.sessionNormale, name="sessionNormale"),
    path("gestiondabsence/", views.gestiondabsence, name="gestiondabsence"),
    
]

