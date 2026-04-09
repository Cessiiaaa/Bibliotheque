from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Livre


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nom = forms.CharField(max_length=100, required=True)
    prenom = forms.CharField(max_length=100, required=True)
    adresse = forms.CharField(max_length=150, required=False)

    class Meta:
        model = User
        fields = ['username','email','nom','prenom','adresse','password1','password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre','auteur', 'genre', 'description', 'date_de_publication',]
        

