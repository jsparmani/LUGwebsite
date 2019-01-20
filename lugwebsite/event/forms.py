from django import forms
from . import models

class EventForm(forms.ModelForm):

	class Meta():
		model = models.Event
		exclude = ['user','created_at']
