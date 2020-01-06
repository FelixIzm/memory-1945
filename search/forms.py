from django import forms
from datetime import date

class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    dateFrom = forms.DateField(auto_now=True, auto_now_add=True, widget=forms.widgets.DateInput(format="%m/%d/%Y"))

