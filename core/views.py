from django.shortcuts import render, redirect, get_object_or_404
from core.models import Annonce, Module, Semestre
from core.forms import AnnonceForm
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm
# Create your views here.


def registre(request):
    form = UserForm()
   # if request.method == 'POST' :
    form =UserForm(data=request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Votre Compte a été bien créer !')
        return redirect('login')
    else:
        messages.warning(request, 'Something is Worng ! Try Again ...')

    return render(request, 'core/registre.html', {'form':form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth_login(request, user)
            if user.isadmine:
                return redirect('index')
            else:
                return redirect('homeProf')
        else:
            messages.warning(request, 'Invalid username or password !')

    return render(request, 'core/login.html')

@login_required
def deconnexion(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    return render(request, 'core/index.html')


@login_required
def annonce(request):
    annonces = Annonce.objects.all()
    context= {
        'annonces': annonces
    }
    return render(request, 'core/annonce.html', context)

@login_required
def deleteAnnonce(request, idAnnonce):
    annonce = Annonce.objects.get(idannonce = idAnnonce)
    annonce.delete()

    return redirect('annonce')

@login_required
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

@login_required
def searchNote(request):
    return render(request, 'core/searchNote.html')

@login_required   
def homeProf(request):
    return render(request, 'Prof/home-prof.html')

@login_required
def chatbot(request):
    return render(request, 'chatbot/chatbot.html')

@login_required
def addAnnonce(request):
    return render(request, 'core/addannonce.html')

@login_required
def correctionNote(request):
    return render(request, 'core/correctionNote.html')

@login_required
def ecours(request):
    return render(request, 'core/ecours.html')

@login_required
def annonceinfos(request):
    return render(request, 'core/annonceinfos.html')

@login_required
def sessionRattrapage(request):
    return render(request, 'admin/sessionRattrapage.html')

@login_required
def sessionNormale(request):
    return render(request, 'admin/sessionNormale.html')

@login_required
def gestiondabsence(request):
    return render(request, 'core/gestiondabsence.html')

@login_required
def profile(request):
    return render(request, 'core/profile.html')

@login_required
def modifypwd(request):
    return render(request, 'core/modifypwd.html')
