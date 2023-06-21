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

    #Reset Password Urlsss*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="resetpasswordlogin/password_reset_form.html"),name='password_reset'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

] 

