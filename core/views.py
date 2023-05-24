from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'core/index.html')

def gestionEtudiant(request):
    return render(request, 'core/gestionEtudiant.html')

def uplaodStudentList(request):
    return render(request, 'core/uploadInscriptionList.html')

def uplaodInscriptionInfos(request):
    return render(request, 'core/uploadInscriptionInfos.html')

def uploadEtudiantFiliere(request):
    return render(request, 'core/uploadEtudiantFiliere.html')