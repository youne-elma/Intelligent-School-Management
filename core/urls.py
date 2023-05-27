from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"), 
    path("addNotesProf/", views.addNotesProf, name="addNotesProf"),  
    path("upload_success/", views.upload_success, name="upload_success"), 
]
