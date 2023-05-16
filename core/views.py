from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def annonce(request):
    return render(request, 'core/annonce.html')

def SearchNote(request):
    return render(request, 'core/SearchNote.html')
    
def homeProf(request):
    return render(request, 'Prof/home-prof.html')
