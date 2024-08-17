from django import forms
from .models import main_model
class main_form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(render_value=False),required=True)
    confirm_password=forms.CharField(widget=forms.PasswordInput(render_value=False),required=True)
    user=forms.CharField(widget=forms.HiddenInput(),initial="patients")
    class Meta:
        model=main_model
        fields="__all__"
    
class Login(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())