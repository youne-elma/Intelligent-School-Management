from core.models import Lecture

def annonces_non_lues(request):
    if request.user.is_authenticated:
        utilisateur = request.user
        lectures_non_lues = Lecture.objects.filter(idutilisateur=utilisateur, is_read=False)
        annonces_non_lues = lectures_non_lues.count()
    else:
        annonces_non_lues = 0

    return {
        'annonces_non_lues': annonces_non_lues
    }
