from django.contrib import admin

from core.models import Etudiant, Professeur

# Register your models here.

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    pass

@admin.register(Professeur)
class ProfesseurAdmin(admin.ModelAdmin):
    pass
