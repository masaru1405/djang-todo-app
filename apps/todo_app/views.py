from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect

from .models import ToDoList, ToDoItem

class ToDoListListView(ListView):
   model = ToDoList
   context_object_name = 'todos'
   template_name = 'todo_app/index.html'

   def get_queryset(self):
      if self.request.user.is_authenticated:
         return self.request.user.lists.all()
      return None

class ToDoListCreateView(LoginRequiredMixin, CreateView):
   model = ToDoList
   fields = ['title']

   def get_context_data(self):
      context = super(ToDoListCreateView, self).get_context_data()
      context['title'] = 'Add a new list'
      return context
   
   def form_valid(self, form):
      self.object = form.save(commit=False)
      self.object.user = self.request.user
      self.object.save()
      return HttpResponseRedirect(self.get_success_url())

class ToDoListDeleteView(LoginRequiredMixin, DeleteView):
   model = ToDoList
   success_url = reverse_lazy('index')

class ToDoItemListView(LoginRequiredMixin, ListView):
   model = ToDoItem
   context_object_name = 'todoitem'
   template_name = "todo_app/todo_list.html"

   def get_queryset(self):
      return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])
   
   def get_context_data(self):
      context = super().get_context_data()
      context['todo_list'] = ToDoList.objects.get(id=self.kwargs["list_id"])
      return context

###ITEM###
class ToDoItemCreateView(LoginRequiredMixin, CreateView):
   model = ToDoItem
   fields = ["todo_list", "title", "description", "due_date"]

   def get_initial(self):
      initial_data = super(ToDoItemCreateView, self).get_initial()
      todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
      initial_data['todo_list'] = todo_list
      return initial_data
   
   def get_context_data(self):
      context = super(ToDoItemCreateView, self).get_context_data()
      todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
      context['todo_list'] = todo_list
      context['title'] = 'Create a new item'
      return context
   
   def get_success_url(self):
      return reverse('list', args=[self.object.todo_list_id])

class ToDoItemUpdateView(LoginRequiredMixin, UpdateView):
   model = ToDoItem
   fields = ["todo_list", "title", "description", "due_date"]

   def get_context_data(self):
      context = super(ToDoItemUpdateView, self).get_context_data()
      context['todo_list'] = self.object.todo_list
      context['title'] = 'Edit item'
      return context
   
   def get_success_url(self):
      return reverse('list', args=[self.object.todo_list_id])


class ToDoItemDeleteView(LoginRequiredMixin, DeleteView):
   model = ToDoItem

   def get_success_url(self):
      return reverse_lazy("list", args=[self.kwargs['list_id']])
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['todo_list'] = self.object.todo_list
      return context