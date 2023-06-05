from django.shortcuts import render,redirect
import pandas as pd
from core.models import Examen, Local, Etudiant,Module,utilisateur
from .forms import FileUploadForm,NoteForm
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render, redirect, get_object_or_404
from core.models import Annonce, Module, Semestre, Etudiant
from datetime import datetime
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm
from datetime import datetime, time


# Create your views here.

def registre(request):
    try:
        form = UserForm()
    # if request.method == 'POST' :
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre Compte a été bien créer !')
            return redirect('login')
        else:
            print(form.errors)
        return render(request, 'core/registre.html', {'form':form})
    except Exception as e:
        form = UserForm()
        messages.warning(request, e)
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
                return redirect('index')
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
def addNotesProf(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        module_id = request.POST.get('module')
       
        if Module.objects.filter(id_modmat=module_id, idutilisateur=request.user.idutilisateur).exists():
            print(module_id , request.user.idutilisateur)


        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            columns = df.columns
            try:
                for _, row in df.iterrows():
                    for column_name in columns:
                        if column_name.lower() == 'id_modmat':
                            if row[column_name] != module_id:
                                messages.error(request, "Invalid module ID, please check your file and try again !")
                                return redirect('addNotesProf')
                    examen = Examen()
                    for column_name in columns:
                        if column_name.lower() == 'id_local':
                            
                            local_value = row[column_name]
                            local = Local.objects.get(id_local=local_value)
                            print(local.id_local)
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
             
                return redirect('showNotes')
            except Exception as e:
                print(e)
                messages.error(request, "please check your file and try again !" + str(e.args[1]))
                return redirect('addNotesProf')
    
    return render(request, 'core/addNotesProf.html')

@login_required
def upload_success(request):
    return render(request, 'core/upload_success.html')

@login_required
def Notes(request):
    return render(request, 'core/Notes.html')


@login_required
def showNotes(request):
    notes = Examen.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'core/showNotes.html', context)

@login_required
def deleteNote(request, idNotes):

    examen = Examen.objects.get(id = idNotes)
    examen.delete()

    

    return redirect('showNotes')


def test(request):
    examen = Examen.objects.all()
    for examens in examen:
        print(examens.id_local)
    return render(request, 'core/test.html')


@require_GET
def get_object(request, object_id):
    try:
        # Query the database for the object with the provided ID
        Note = Examen.objects.get(id=object_id)
        student = Etudiant.objects.get(apogee=Note.apogee.apogee)
        # Build the response data
        data = {
            'Name': student.nomfr + " " + student.prenomfr,
            'apogee': Note.apogee.apogee,
            'note': Note.note,
            'session': Note.session,
            'date': Note.h_debut,
            # ... other attributes
        }
        return JsonResponse(data)
    except Examen.DoesNotExist:
        return JsonResponse({'error': 'Object not found'}, status=404)
    except Etudiant.DoesNotExist:
        return JsonResponse({'error': 'Object not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    



@login_required
def addNote(request):
    form = NoteForm()
    etudiants = Etudiant.objects.all()
    salles = Local.objects.all()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, 'Note a été bien ajouter !')
            return redirect('showNotes')
        
    context = {
        'form': form
        ,
        'etudiants': etudiants,
        'salles': salles
    }    
    
        

    return render(request, 'core/addNote.html',context)