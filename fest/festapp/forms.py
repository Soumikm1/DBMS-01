# forms.py
from django import forms
from .models import Event

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_date', 'event_name', 'event_type', 'thumbnail']
