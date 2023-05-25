from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'core/index.html')

def gestionEtudiant(request):
    return render(request, 'core/gestionEtudiant.html')

def uploadStudentList(request):
    return render(request, 'core/uploadStudentList.html')

def uplaodInscriptionInfos(request):
    return render(request, 'core/uploadInscriptionInfos.html')

def uploadEtudiantFiliere(request):
    return render(request, 'core/uploadEtudiantFiliere.html')