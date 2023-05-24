from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gestionEtudiant/", views.gestionEtudiant, name="gestionEtudiant"),
    path("gestionEtudiant/uploadStudentList/", views.uplaodStudentList, name="uploadStudentList"),
    path("gestionEtudiant/uploadInscriptionList/", views.uplaodInscriptionInfos, name="uploadInscriptionList")
   ,path("gestionEtudiant/uploadEtudiantFiliere/", views.uploadEtudiantFiliere, name="uploadEtudiantFiliere")
]
