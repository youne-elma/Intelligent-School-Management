from django.shortcuts import render, redirect, get_object_or_404
from core.models import Annonce, Module, Semestre, Reports, Etudiant, utilisateur, Chat, Examen, Local, Seance
from core.forms import AnnonceForm, AjoutAnnonceForm, SeanceForm, AddSeanceForm
from datetime import datetime
from django.contrib.auth import authenticate, logout, update_session_auth_hash, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import pandas as pd 
from django.views.decorators.http import require_GET
from .forms import UserForm, FileUploadForm, NoteForm, UpdateNoteForm, UpdateSeanceForm
import requests
import json
import os
import csv
from django.http import HttpResponse
from .filters import NoteFilter, SeanceFilter

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
            # request.session.set_expiry(15)
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
def addAnnonce(request):

    etudiants = Etudiant.objects.all()
    modules = Module.objects.all()
    semestres = Semestre.objects.all()


    if request.method == 'POST':

        form = AnnonceForm(request.POST)
        
        if form.is_valid():

            idutilisateur = utilisateur.objects.get(idutilisateur = request.user.idutilisateur)
            titreannonce = form.cleaned_data['titreannonce']
            id_semestre = form.cleaned_data['id_semestre']
            id_modmat = form.cleaned_data['id_modmat']
            contenu = form.cleaned_data['contenu']
            apogee_value = request.POST.get('apogee')
            dateannonce_value = datetime.now()

            if apogee_value == "":
                Annonce.objects.create(titreannonce= titreannonce, id_semestre= id_semestre, id_modmat= id_modmat, contenu= contenu, dateannonce = dateannonce_value, idutilisateur = idutilisateur)

                return redirect('annonce')

            for etudiant in etudiants:
                if(str(etudiant.apogee) == apogee_value):
                    errorApogee = False
                    break
                else:
                    errorApogee = True


            if(errorApogee):

                context = {
                    'errorApogee': errorApogee,
                    'modules': modules,
                    'semestres': semestres,
                }

                return render(request, 'core/addannonce.html', context)
            
            etudiantApogeeValid = Etudiant.objects.get(apogee = int(apogee_value))
            
            Annonce.objects.create(titreannonce= titreannonce, id_semestre= id_semestre, id_modmat= id_modmat, contenu= contenu, dateannonce = dateannonce_value, apogee = etudiantApogeeValid, idutilisateur = idutilisateur)

            return redirect('annonce')

        else:
            print(form.errors)

    else:
        form = AjoutAnnonceForm()

    context = {
        'modules': modules,
        'semestres': semestres,
    }

    return render(request, 'core/addannonce.html', context)

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
def correctionNote(request):
    return render(request, 'core/correctionNote.html')

@login_required
def ecours(request):
    return render(request, 'core/ecours.html')

@login_required
def annonceinfos(request, idAnnonce):

    annonce = get_object_or_404(Annonce, idannonce=idAnnonce)
    context= {
        'annonce': annonce
    }

    return render(request, 'core/annonceInfos.html', context)

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
    if request.method == 'POST' and request.FILES.get('profile_image'):
        profile_image = request.FILES['profile_image']
        user = request.user
        if user.profilepic:
            user.profilepic.delete(save=False)
        request.user.profilepic = profile_image
        request.user.save()
        return redirect('profile')
        
    return render(request, 'core/profile.html')

@login_required
def modifypwd(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data= request.POST, user= request.user)

        try: 
            confirmation = request.POST['confirmation'] == 'on'
            print(confirmation)
        except:
            confirmation = False
        if form.is_valid() and confirmation :
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'core/modifypwd.html', { 'modifySuccess': True })
        else:
            return render(request, 'core/modifypwd.html', {'form':form.errors,'confirmation': confirmation})
    else:
        form = PasswordChangeForm(user= request.user)
    
    return render(request, 'core/modifypwd.html')


@login_required
def send(request):
    sender = utilisateur.objects.get(idutilisateur = request.user.idutilisateur)
    receiver = utilisateur.objects.get(idutilisateur = 10)
    message = request.POST.get('message')
    
    #api
    url = "https://langchain-chat-v3.herokuapp.com/predict"
    headers = {'Content-Type': 'application/json'}
    payload = {
                "user_input": {
                    "text": message
                },
                "chat_history": {
                    "list": []
                }
            }
    if request.method == 'POST':
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        new_message = Chat.objects.create(user_id=sender, destination=receiver, message=message, date=datetime.now())
        new_message.save()
        print (response.status_code)
        if( response.status_code == 200):
            try:
               
                answer = response.json()['answer'] 
                new_message = Chat.objects.create(user_id=receiver, destination=sender, message=answer, date=datetime.now())
                new_message.save()
                return JsonResponse({"answer": answer } )
            except Exception as e:
                answer = str(e)
                new_message = Chat.objects.create(user_id=receiver, destination=sender, message=answer, date=datetime.now())
                new_message.save()

                return JsonResponse({"answer": str(e) })
        else : 
                answer = response.json()['error']
                new_message = Chat.objects.create(user_id=receiver, destination=sender, message=answer, date=datetime.now())
                new_message.save()
                return JsonResponse({"answer": answer })

    
    return redirect('chatbot')

def getMessages(request):

    user_messages = Chat.objects.filter(user_id = request.user.idutilisateur)
    bot_messagees = Chat.objects.filter(destination = request.user.idutilisateur)

    return JsonResponse({"user":list(user_messages.values()) , "bot":list(bot_messagees.values())})
    

def bugreport(request):
    
    if request.method == 'POST':
        bug = request.POST.get('message')
        localHist = request.POST.get('localHist')
        new_bug = Reports.objects.create(report_message  = bug, date = datetime.now(), log = localHist)
        new_bug.save()
        print(new_bug)
        return JsonResponse({"answer": 'ok'})

    return JsonResponse({"answer": 'ok'})   

def bugreportsuccess(request):
    if request.method == "GET":
         return redirect('chatbot')

    

# login_required
#def getMessages(request, room):
#    room_details = Room.objects.get(name=room)
#
#    messages = Message.objects.filter(room=room_details.id)
#    return JsonResponse({"messages":list(messages.values())})

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
    Etudiants = Etudiant.objects.all()
    notes = Examen.objects.all()
    myFilter = NoteFilter(request.GET, queryset=notes)
    notes = myFilter.qs
    context = {
        'notes': notes,
        'Etudiants': Etudiants,
        'myFilter': myFilter
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
        'form': form,
        'etudiants': etudiants,
        'salles': salles
    }    
    
        

    return render(request, 'core/addNote.html',context)


@login_required
def download(request):
 
    # Create a CSV file as an example
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="TemplateNote.csv"'

    # Write data to the CSV file
    writer = csv.writer(response)
    writer.writerow(['ID_LOCAL', 'APOGEE', 'ID_MODMAT', 'N_EXAMEN', 'h_Debut', 'h_Fin', 'RESULTAT', 'NOTE', 'SESSION'])
    print(request.user.idutilisateur)
    print("test")
    return response


@login_required
def updateNote(request, idNote):

    examen = get_object_or_404(Examen, id=idNote)
    modules = request.user.module_set.all()
    semestres = Semestre.objects.all()
    etudiant = get_object_or_404(Etudiant, apogee=examen.apogee.apogee)
    
    if(request.method == 'POST'):
          
        form = UpdateNoteForm(request.POST, instance=examen)

        if form.is_valid():
           try:
            
            examen.h_debut = form.cleaned_data['h_debut']
            examen.session = form.cleaned_data['session']
            examen.note = form.cleaned_data['note']
            examen.id_modmat = form.cleaned_data['id_modmat']
            examen.id_local = form.cleaned_data['id_local']
            examen.n_examen = form.cleaned_data['n_examen']
           
            examen.save(update_fields=['h_debut','session' , 'note','n_examen','id_local','id_modmat'])
           except Exception as e:
               print(e) 
        else:
            print(form.errors)

        return redirect('showNotes')

    context = {
        'note': examen,
        'modules': modules,
        'semestres': semestres,
        
        'salles' : Local.objects.all()}

    return render(request, 'core/modifyNote.html', context)

@login_required
def gestionSeance(request):
    return render(request, 'core/gestionSeance.html')

@login_required
def showSeances(request):
    seances = Seance.objects.filter(idutilisateur = request.user.idutilisateur)
    modules = Module.objects.all()
    semestres = Semestre.objects.all()
    myFilter = SeanceFilter(request.GET, queryset=seances)
    seances = myFilter.qs

    context = {
        'seances': seances,
        'modules': modules,
        'semestres': semestres,
    }
    return render(request, 'core/showSeances.html', context)


@login_required
def addSeance(request):
    modules = Module.objects.all()
    semestres = Semestre.objects.all()


    if request.method == 'POST':

        form = AddSeanceForm(request.POST)
        
        
        if form.is_valid():

            idutilisateur = utilisateur.objects.get(idutilisateur = request.user.idutilisateur)
            titreseance = form.cleaned_data['titreseance']
            id_modmat = form.cleaned_data['id_modmat']
            id_semestre = form.cleaned_data['id_semestre']
            datedebut = request.POST.get('datedebut')
            datefin = request.POST.get('datefin')

            details = request.POST.get('details')
            groupe = request.POST.get('groupe')
            filiere = request.POST.get('filiere')
            section = request.POST.get('section')

            datedebut = datedebut.replace("T", " ")
            datefin = datefin.replace("T", " ")


            if datedebut == "" or datefin == "":
                Seance.objects.create(titreseance= titreseance, id_semestre= id_semestre, id_modmat= id_modmat, details= details, idutilisateur= idutilisateur, groupe= groupe, filiere= filiere, section= section)
            else :
                Seance.objects.create(titreseance= titreseance, id_semestre= id_semestre, id_modmat= id_modmat, details= details, datedebut= datedebut, datefin= datefin, idutilisateur= idutilisateur, groupe= groupe, filiere= filiere, section= section)

            messages.success(request, 'Séance a été bien ajouter !')
            return redirect('showSeances')

        else:
            print(form.errors)

    else:
        form = SeanceForm()

    context = {
        'modules': modules,
        'semestres': semestres,

    }
    
    return render(request, 'core/addSeance.html', context)

@login_required
def deleteSeance(request, idSeance):
    seance = Seance.objects.get(idseance = idSeance)
    seance.delete()

    messages.success(request, 'Séance a bien été supprimé !')
    return redirect('showSeances')



def updateSeance(request, idSeance):
    seance = get_object_or_404(Seance, idseance=idSeance)
    modules = Module.objects.all()
    semestres = Semestre.objects.all()
    
    if(request.method == 'POST'):
        
        form = UpdateSeanceForm(request.POST, instance=seance)

        if form.is_valid():
           try:
            
            seance.id_modmat = form.cleaned_data['id_modmat']
            seance.titreseance = form.cleaned_data['titreseance']
            datedebut = request.POST.get('datedebut')
            datefin = request.POST.get('datefin')
            seance.details = request.POST.get('details')
            seance.groupe = request.POST.get('groupe')
            seance.filiere = request.POST.get('filiere')
            seance.section = request.POST.get('section')

            seance.datedebut = datedebut.replace("T", " ")
            seance.datefin = datefin.replace("T", " ")
            
            if datedebut == "" and datefin != "":
                seance.save(update_fields=['id_modmat', 'titreseance', 'details', 'groupe', 'filiere', 'section', 'datefin'])
            elif datedebut != "" and datefin == "" :
                seance.save(update_fields=['id_modmat', 'titreseance', 'details', 'groupe', 'filiere', 'section', 'datedebut'])
            else:
                seance.save(update_fields=['id_modmat', 'titreseance', 'datedebut', 'datefin', 'details', 'groupe', 'filiere', 'section'])
           except Exception as e:
               print(e)
        else:
            print(form.errors)

        return redirect('showSeances')



    context = {
        'seance': seance,
        'modules': modules,
        'semestres': semestres,
    }

    return render(request, 'core/updateSeance.html', context)


@login_required
def seanceInfos(request,idSeance):
    seance = get_object_or_404(Seance, idseance= idSeance)
    context= {
        'seance': seance,
    }

    return render(request, 'core/seanceInfos.html', context)