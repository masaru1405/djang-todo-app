from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from .forms import SignUpForm, LoginForm

class LoginInterfaceView(LoginView):
   form_class = LoginForm
   template_name = 'members/login.html'

   def get(self, request, *args, **kwargs):
      if self.request.user.is_authenticated:
         return redirect('index')
      return super().get(request, *args, **kwargs)

class UserRegisterView(CreateView):
   form_class = SignUpForm
   template_name = 'members/register.html'
   success_url = reverse_lazy('login')

   def get(self, request, *args, **kwargs):
      if self.request.user.is_authenticated:
         return redirect('index')
      return super().get(request, *args, **kwargs)