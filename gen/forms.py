from django import forms
from .models import CSVData
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



CHOICES = (

    ('1', 'Choose...'),
    ('2', 'name'),
    ('3','job'),
    ('4', 'email'),
    ('5', 'domail'),
    ('6', 'phone'),
    ('7', 'company'),
    ('8','text'),
    ('9', 'integer'),
    ('9', 'address'),
    ('10', 'date'),


    )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='User name', widget = forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', widget = forms.PasswordInput(attrs={'class':'form-control'}))

class CSVDataForm(forms.Form):
    name = forms.CharField()
    num_rows = forms.IntegerField(min_value=1, max_value=1000)
    min_value = forms.IntegerField()
    max_value = forms.IntegerField()

class CSVDataForm_e(forms.ModelForm):
    class Meta:
        model = CSVData
        fields = ['name']