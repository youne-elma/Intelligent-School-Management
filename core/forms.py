from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import Annonce, utilisateur, Specialite, Departement, Examen, Seance

class UpdateSeanceForm(forms.ModelForm):
    class Meta:
        model = Seance
        fields= ['titreseance', 'id_modmat', 'id_semestre']

class SeanceForm(forms.ModelForm):
    class Meta:
        model = Seance
        fields = ['titreseance', 'id_modmat', 'id_semestre', 'groupe', 'filiere', 'datefin', 'datedebut', 'details', 'section', 'salle']

class AddSeanceForm(forms.ModelForm):
    class Meta:
        model = Seance
        fields = ['titreseance', 'id_modmat', 'id_semestre']

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ['titreannonce', 'contenu','id_semestre', 'id_modmat']

class AjoutAnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ['titreannonce', 'contenu' ,'id_semestre', 'id_modmat', 'apogee']


class FileUploadForm(forms.Form):
    file = forms.FileField()

class NoteForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = ['apogee', 'h_debut', 'session', 'note', 'id_modmat', 'id_local','n_examen']
   
    
class UpdateNoteForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = ['h_debut', 'session', 'note', 'id_modmat', 'id_local','n_examen']    

        
class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        #Choices name from table specialite 
        specs = Specialite.objects.all()
        self.fields['idspec'].choices=[(spec.idspec, spec.intitulespec) for spec in specs]
        #Choices name from table Departement 
        depts = Departement.objects.all()
        self.fields['iddept'].choices=[(dept.iddept, dept.intituledept) for dept in depts]

    class Meta:
        model = utilisateur
        fields = [
            'cin',
            'n_som',
            'nomar',
            'prenomar',
            'nomfr',
            'prenomfr',
            'telephone',
            'email',
            'username',
            'password1',
            'password2',
            'idspec',
            'iddept',
            'isadmine'
        ]
        # widgets = {
        #     'cin':forms.TextInput(attrs={'class': 'text-xl'}),
        #     'n_som': forms.TextInput(attrs={'class': 'text-xl'}),
        # }
