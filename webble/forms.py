from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Book


class RegistrationForm(UserCreationForm):
    country = forms.CharField(required=True, max_length=20)

    class Meta:
        model = User
        fields = ['username', 'country', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save()
        if commit:
            user.save()
        return user


class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
