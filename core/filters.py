import django_filters
from .models import *
from django_filters import DateFilter

from django import forms


class NoteFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="h_debut", lookup_expr='gte')
    id_modmat = django_filters.ModelChoiceFilter(
        queryset=Module.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    apogee = django_filters.ModelChoiceFilter(
        queryset=Etudiant.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model  = Examen
        fields = ['apogee','session','id_modmat']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'widget': forms.TextInput(attrs={'class': 'gestionEtudiants:self-center rounded-[5px] text-[0.9rem] w-[200px] py-2'})
                },
            },
            models.DateField: {
                'filter_class': django_filters.DateFilter,
                'extra': lambda f: {
                    'widget': forms.DateInput(attrs={'class': 'gestionEtudiants:self-center rounded-[5px] text-[0.9rem] w-[200px] py-2', 'type': 'date'})
                },
            },
            models.ForeignKey: {
                'filter_class': django_filters.ChoiceFilter,
                'extra': lambda f: {
                    'widget': forms.Select(attrs={'class': 'gestionEtudiants:self-center rounded-[5px] text-[0.9rem] w-[200px] py-2'})
                },
            },
            # Add more overrides for other field types as needed
        }
        