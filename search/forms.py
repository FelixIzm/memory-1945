from django import forms
from datetime import date

class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    date_From = forms.DateField(initial=date.today, widget=forms.widgets.DateInput(format="%d.%m.%Y"))
    date_To = forms.DateField(initial=date.today, widget=forms.widgets.DateInput(format="%d.%m.%Y"))

