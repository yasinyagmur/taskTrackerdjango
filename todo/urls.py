from django.urls import path, include
from .views import (
    # todo_list_create,
    todo_home,
    # todo_detail,
    TodoDetail,
    Todos, TodoMVS
)

from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo', TodoMVS)

urlpatterns = [
    path('', todo_home),
    # path('list-create/', todo_list_create),
    # path('detail/<int:id>', todo_detail),
    path('list-create/', Todos.as_view()),
    path('detail/<int:id>', TodoDetail.as_view()),
    path("", include(router.urls))
]


# urlpatterns += router.urls
