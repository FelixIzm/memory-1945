from django import forms
from datetime import date
from datetime import datetime

class UserForm(forms.Form):
    d_from = "01-05-1945"
    d_to = "31-05-1945"
    unit = forms.CharField(label='Воинское подразделение')
    date_From = forms.CharField(initial=datetime.strptime(d_from, "%d-%m-%Y").date(), widget=forms.widgets.DateInput(format="%d.%m.%Y"), label='Дата начала', required=False)
    date_To = forms.CharField(initial=datetime.strptime(d_to, "%d-%m-%Y").date(), widget=forms.widgets.DateInput(format="%d.%m.%Y"), label ='Дата окончания', required=False)
