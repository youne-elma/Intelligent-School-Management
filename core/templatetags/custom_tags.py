from django import template
from core.models import Lecture

register = template.Library()

@register.filter
def is_read(annonce, user):
    try:
        lecture = Lecture.objects.get(idannonce=annonce.idannonce, idutilisateur=user.idutilisateur)
        return lecture.is_read
    except Lecture.DoesNotExist:
        return False