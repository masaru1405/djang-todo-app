from django.urls import path
from . import views

urlpatterns = [
   path('', views.ToDoListListView.as_view(), name='index'),
]