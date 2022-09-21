from django.urls import path
from . import views

urlpatterns = [
   path('', views.ToDoListListView.as_view(), name='index'),
   path('list/<int:list_id>', views.ToDoItemListView.as_view(), name='list'),
   #CRUD patterns for ToDoLists
   path('list/add', views.ToDoListCreateView.as_view(), name='list-add'),
   #CRUD patterns for ToDoItems
   path('list/<int:list_id>/item/add', views.ToDoItemCreateView.as_view(), name='item-add'),
   path('list/<int:list_id>/item/<int:pk>', views.ToDoItemUpdateView.as_view(), name='item-update'),
]