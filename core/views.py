from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def login(request):
    return render(request, 'core/login.html')

def annonce(request):
    return render(request, 'core/annonce.html')

def handling_404(request, exception):
    return render(request, 'core/404.html', status=404)