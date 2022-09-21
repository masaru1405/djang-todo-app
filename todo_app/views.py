from django.shortcuts import render
from django.views.generic import ListView

from .models import ToDoList, ToDoItem

class ToDoListListView(ListView):
   model = ToDoList
   context_object_name = 'todos'
   template_name = 'todo_app/index.html'

class ToDoItemListView(ListView):
   model = ToDoItem
   context_object_name = 'todoitem'
   template_name = "todo_app/todo_list.html"

   def get_queryset(self):
      return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])
   
   def get_context_data(self):
      context = super().get_context_data()
      context['todo_list'] = ToDoList.objects.get(id=self.kwargs["list_id"])
      return context
