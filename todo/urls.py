from django.urls import path
from .views import todo_list_create, todo_home, todo_detail

urlpatterns = [
    path('', todo_home),
    path('list-create/', todo_list_create),
    path('detail/<int:id>', todo_detail),
]
