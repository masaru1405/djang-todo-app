from django.urls import path
from . import views

urlpatterns = [
   path('register', views.UserRegisterView.as_view(), name='register'),
   path('login', views.LoginInterfaceView.as_view(), name='login'),
   path('logout', views.LogoutInterfaceView.as_view(), name='logout')
]