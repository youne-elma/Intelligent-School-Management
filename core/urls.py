from django.urls import path
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views


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
    path('gestionSeance/', views.gestionSeance, name='gestionSeance'),
    path('gestionSeance/showSeances/', views.showSeances, name="showSeances"),
    path('gestionSeance/addSeance/', views.addSeance, name="addSeance"),
    path('gestionSeance/updateSeance/<str:idSeance>', views.updateSeance, name="updateSeance"),
    path("gestionSeance/deleteSeance/<str:idSeance>/", views.deleteSeance, name="deleteSeance"),
    path("gestionSeance/addSeance/", views.addSeance, name="addSeance"),
    path("gestionSeance/seanceInfos/<str:idSeance>", views.seanceInfos, name="seanceInfos"),

    #Reset Password Urlsss*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="resetpasswordlogin/password_reset_form.html"),name='password_reset'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(template_name="resetpasswordlogin/password_reset_done.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="resetpasswordlogin/password_reset_confirm.html"),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="resetpasswordlogin/password_reset_complete.html"),name='password_reset_complete'),

] 

