from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from .forms import SignUpForm

def login(request):
   return HttpResponse('Login')

class UserRegisterView(CreateView):
   form_class = SignUpForm
   template_name = 'members/register.html'
   success_url = reverse_lazy('login')