from django import forms
from datetime import date
from django.utils import timezone

class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    dateFrom = forms.DateField(default=timezone.now)

