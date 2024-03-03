from django import template
from festapp.models import Registration

register = template.Library()

@register.filter(name='is_registered')
def is_registered(user, event):
    return Registration.objects.filter(user=user, event=event).exists()
