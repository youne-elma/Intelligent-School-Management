from django.shortcuts import render, redirect, get_object_or_404
from core.models import Annonce, Module, Semestre,Reports, Etudiant, utilisateur,Chat
from core.forms import AnnonceForm, AjoutAnnonceForm
from datetime import datetime
from django.contrib.auth import authenticate, logout, update_session_auth_hash, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .forms import UserForm
import requests
import json
import os

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

    print(request.POST)

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
        print(request.POST)
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

    

login_required
#def getMessages(request, room):
#    room_details = Room.objects.get(name=room)
#
#    messages = Message.objects.filter(room=room_details.id)
#    return JsonResponse({"messages":list(messages.values())})