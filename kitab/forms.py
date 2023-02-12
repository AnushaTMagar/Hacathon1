from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_no = forms.CharField(max_length=10)
    

    class meta:
        model = User
        fields =("username","email","password")

    def save(self, commit: True):
        user = super(RegistrationForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
        