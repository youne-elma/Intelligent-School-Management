from django.shortcuts import render
from models import Etablissementbp
# Create your views here.


def index(request):
    return render(request, 'core/index.html')

def test(request):
    record = Etablissementbp.objects.all()
    return render(request, 'core/test.html',{'record',record})
