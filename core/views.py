from django.shortcuts import render, redirect
from core.models import Annonce

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

# context = {}

# return render(request, 'core/annonce.html', context)

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

