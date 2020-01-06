from django import forms
from datetime import date

class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    dateFrom = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))

