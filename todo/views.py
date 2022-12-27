from django.shortcuts import render


from .models import Todo
from .serializers import TodoSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view()
def todo_home(request):
    return Response({'home': 'This is todo home page'})


@api_view(['GET', 'POST'])
def todo_list_create(request):
    if request.method == "GET":
        todos = Todo.objects.filter(is_done=False)
        seralizer = TodoSerializers(todos, many=True)
        return Response(seralizer.data)

    if request.method == "POST":
        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid():
            seralizer.save()
            return Response(seralizer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)

    if request.method == "GET":
        # todo = get_object_or_404(Todo, id=id)
        serializer = TodoSerializers(todo)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = TodoSerializers(data=request.data, instance=todo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        todo.delete()
        return Response({'message': 'Todo deleted succesfuly'})
