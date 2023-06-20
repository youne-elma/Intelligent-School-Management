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
    path("Notes/addNotesProf/", views.addNotesProf, name="addNotesProf"),  
    path("Notes/upload_success/", views.upload_success, name="upload_success"), 
    path("Notes/", views.Notes, name="Notes"),
    path("Notes/showNotes/", views.showNotes, name="showNotes"),
    path("Notes/deleteNote/<str:idNotes>/", views.deleteNote, name="deleteNote"),
    path("test/", views.test, name="test"),
    path('api/objects/<int:object_id>/', views.get_object, name='get_object'),
    path("login/", views.login, name="login"), 
    path("addNote/", views.addNote, name="addNote"), #addNote
    path('download/', views.download, name='download'),
    path('updateNote/<str:idNote>/', views.updateNote, name='updateNote'),

] 

