from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import Annonce, utilisateur

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ['titreannonce', 'contenu','id_semestre', 'id_modmat']

class UserForm(UserCreationForm):
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
            'isadmine'
        ]
