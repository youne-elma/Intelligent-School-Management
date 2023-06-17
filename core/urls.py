from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("deconnexion/", views.deconnexion, name="deconnexion"),
    path("accounts/login/", views.login, name="login"), 
    path("registre/", views.registre, name="registre"), #registre
    path("annonce/",views.annonce,name="annonce"),
    path("searchNote/",views.searchNote,name="searchNote"),
    path("homeProf/", views.homeProf, name="homeProf"),
    path("chatbot/", views.chatbot, name="chatbot"),
    path("addannonce/", views.addAnnonce, name="addAnnonce"),
    path("correctionNote/", views.correctionNote, name="correctionNote"),
    path("ecours/", views.ecours, name="ecours"),
    path("annonceinfos/<str:idAnnonce>", views.annonceinfos, name="annonceinfos"),
    path("sessionRattrapage/", views.sessionRattrapage, name="sessionRattrapage"),
    path("sessionNormale/", views.sessionNormale, name="sessionNormale"),
    path("gestiondabsence/", views.gestiondabsence, name="gestiondabsence"),
    path("profile/",views.profile,name="profile"),
    path("modifypwd/",views.modifypwd,name="modifypwd"),
    path("annonce/updateAnnonce/<str:idAnnonce>", views.updateAnnonce, name="updateAnnonce"),
    path("deleteAnnonce/<str:idAnnonce>/", views.deleteAnnonce, name="deleteAnnonce"),
    path("send", views.send, name="send"),
    path("getMessages", views.getMessages, name="getMessages"),
    path("bugreport", views.bugreport, name="bugreport"),
    path("bugreportsuccess ", views.bugreportsuccess , name="bugreportsuccess "),

] 

