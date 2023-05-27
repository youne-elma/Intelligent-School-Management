from django.shortcuts import render,redirect
import pandas as pd
from core.models import Examen, Local, Etudiant,Module
from .forms import FileUploadForm

# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def login(request):
    return render(request, 'core/login.html')



def addNotesProf(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            columns = df.columns

            for _, row in df.iterrows():
                examen = Examen()
                for column_name in columns:
                    if column_name.lower() == 'id_local':
                        local_value = row[column_name]
                        local = Local.objects.get(id_local=local_value)
                        setattr(examen, column_name.lower(), local)
                    elif column_name.lower() == 'apogee':
                        apogee_value = row[column_name]
                        etudiant = Etudiant.objects.get(apogee=apogee_value)    
                        setattr(examen, column_name.lower(), etudiant)
                    elif column_name.lower() == 'id_modmat':
                        module_value = row[column_name]
                        module = Module.objects.get(id_modmat=module_value)
                        setattr(examen, column_name.lower(), module)
                    else:
                        setattr(examen, column_name.lower(), row[column_name])
                examen.save()

            return redirect('upload_success')
    
    return render(request, 'core/addNotesProf.html')

def upload_success(request):
    return render(request, 'core/upload_success.html')

def Notes(request):
    return render(request, 'core/Notes.html')

def showNotes(request):
    notes = Examen.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'core/showNotes.html', context)