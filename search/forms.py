from django import forms

class UserForm(forms.Form):
    name = forms.CharField()
    age1 = forms.IntegerField()
    #dateFrom = forms.DateField()
