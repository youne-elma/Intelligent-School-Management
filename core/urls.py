from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"), 
    path("Notes/addNotesProf/", views.addNotesProf, name="addNotesProf"),  
    path("Notes/upload_success/", views.upload_success, name="upload_success"), 
    path("Notes/", views.Notes, name="Notes"),
    path("Notes/showNotes/", views.showNotes, name="Notes"),
]
