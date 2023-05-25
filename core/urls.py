from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gestionEtudiant/", views.gestionEtudiant, name="gestionEtudiant"),
    path("gestionEtudiant/uploadStudentList/", views.uploadStudentList, name="uploadStudentList"),
    path("gestionEtudiant/uploadInscriptionInfos/", views.uplaodInscriptionInfos, name="uploadInsciprtionInfos")
   ,path("gestionEtudiant/uploadEtudiantFiliere/", views.uploadEtudiantFiliere, name="uploadEtudiantFiliere")
]
