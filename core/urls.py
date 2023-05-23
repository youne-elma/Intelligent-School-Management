from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gestionEtudiant/", views.gestionEtudiant, name="gestionEtudiant"),
    path("gestionEtudiant/uplaodStudentList/", views.uplaodStudentList, name="uplaodStudentList"),
]
