from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_todo_items),
    path('insert_Todo/', views.insert_todo_item, name='insert_todo_item'),
    path('delete_Todo/<int:todo_id>',  views.delete_todo_item, name='delete_todo_item'),
]