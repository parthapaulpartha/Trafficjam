from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import postcreate, City,Contact,Comment
from django.forms import TextInput


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class SigninForm(forms.Form):
    username = forms.CharField(label='',widget=  forms.TextInput(attrs={'placeholder':'User name'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class Editprofile(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
        ]

class createform(forms.ModelForm):
    class Meta:
        model = postcreate
        fields = [
            'name',
            'place_name',
            'trafficjam_details',
            'date_and_time'
        ]

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'message'
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment',
            'date_and_time',
        ]
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'Please Comment here '})}



