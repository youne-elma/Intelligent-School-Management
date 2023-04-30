from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def login(request):
    return render(request, 'core/login.html')

def homeProf(request):
    return render(request, 'Prof/home-prof.html')
