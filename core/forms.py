from django import forms
from core.models import Annonce

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ['titreannonce', 'contenu','id_semestre', 'id_modmat']