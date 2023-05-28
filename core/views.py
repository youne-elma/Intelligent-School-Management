from django.shortcuts import render, redirect, get_object_or_404
from core.models import Annonce, Module, Semestre
from core.forms import AnnonceForm

# Create your views here.


def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')


def annonce(request):
    annonces = Annonce.objects.all()
    context= {
        'annonces': annonces
    }
    return render(request, 'core/annonce.html', context)


def deleteAnnonce(request, idAnnonce):
    annonce = Annonce.objects.get(idannonce = idAnnonce)
    annonce.delete()

    return redirect('annonce')


def updateAnnonce(request, idAnnonce):

    annonce = get_object_or_404(Annonce, idannonce=idAnnonce)
    modules = Module.objects.all()
    semestres = Semestre.objects.all()

    if(request.method == 'POST'):

        form = AnnonceForm(request.POST, instance=annonce)

        if form.is_valid():

            annonce.titreannonce = form.cleaned_data['titreannonce']
            annonce.id_semestre = form.cleaned_data['id_semestre']
            annonce.id_modmat = form.cleaned_data['id_modmat']
            annonce.contenu = form.cleaned_data['contenu']

            annonce.save(update_fields=['titreannonce','contenu' , 'id_semestre','id_modmat'])
        else:
            print(form.errors)

        return redirect('annonce')

    context = {
        'annonce': annonce,
        'modules': modules,
        'semestres': semestres
    }

    return render(request, 'core/updateAnnonce.html', context)


def searchNote(request):
    return render(request, 'core/searchNote.html')
    
def homeProf(request):
    return render(request, 'Prof/home-prof.html')

def chatbot(request):
    return render(request, 'chatbot/chatbot.html')

def addAnnonce(request):
    return render(request, 'core/addannonce.html')

def correctionNote(request):
    return render(request, 'core/correctionNote.html')

def ecours(request):
    return render(request, 'core/ecours.html')

def annonceinfos(request):
    return render(request, 'core/annonceinfos.html')

def sessionRattrapage(request):
    return render(request, 'admin/sessionRattrapage.html')

def sessionNormale(request):
    return render(request, 'admin/sessionNormale.html')

def gestiondabsence(request):
    return render(request, 'core/gestiondabsence.html')

def profile(request):
    return render(request, 'core/profile.html')

def modifypwd(request):
    return render(request, 'core/modifypwd.html')
