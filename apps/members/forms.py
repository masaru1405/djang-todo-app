from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
   username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
   password1 = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
   password2 = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Confirmation'}))
   email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
   first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
   last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

   class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

      def clean_email(self):
         email = self.cleaned_data['email']
         if User.objects.filter(email=email).exists():
            raise ValidationError('An user with this email already exists.')
         return email