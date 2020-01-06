from django import forms
from datetime import date
import datetime

class UserForm(forms.Form):
    d_from = "01-01-1939"
    d_to = "01-01-1946"
    unit = forms.CharField(label='Воинское подразделение')
    date_From = forms.DateField(initial=datetime.strptime(d_from, "%d-%m-%Y").date(), widget=forms.widgets.DateInput(format="%d.%m.%Y"))
    date_To = forms.DateField(initial=datetime.strptime(d_to, "%d-%m-%Y").date(), widget=forms.widgets.DateInput(format="%d.%m.%Y"))

