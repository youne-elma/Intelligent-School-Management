from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"), 
    path("Notes/addNotesProf/", views.addNotesProf, name="addNotesProf"),  
    path("Notes/upload_success/", views.upload_success, name="upload_success"), 
    path("Notes/", views.Notes, name="Notes"),
    path("Notes/showNotes/", views.showNotes, name="showNotes"),
    path("Notes/deleteNote/<str:idNotes>/", views.deleteNote, name="deleteNote"),
    path("test/", views.test, name="test"),
    path('api/objects/<int:object_id>/', views.get_object, name='get_object'),
    path("login/", views.login, name="login"), 
    path("accounts/login/", views.login, name="login"), 
    path("registre/", views.registre, name="registre"), #registre
    path("addNote/", views.addNote, name="addNote"), #addNote
    path('download/', views.download, name='download'),
]
