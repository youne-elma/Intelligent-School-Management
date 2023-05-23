from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'core/index.html')

def gestionEtudiant(request):
    return render(request, 'core/gestionEtudiant.html')

def uplaodStudentList(request):
    return render(request, 'core/uplaodStudentList.html')