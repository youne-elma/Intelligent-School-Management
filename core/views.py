from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def annonce(request):
    return render(request, 'core/annonce.html')

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
