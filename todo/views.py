from django.shortcuts import render

# Create your views here.
from todo.serializers import TodoSerializer
from todo.models import Todo

from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ListTodoAPIView(ListAPIView):
    # This endpoint will return the list of all available todo lists
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CreateTodoAPIView(CreateAPIView):
    # This endpoint will create todo list entry
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UpdateTodoAPIView(UpdateAPIView):
    # This endpoint update to todo list by passing id in the url
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer      

class DeleteTodoAPIView(DestroyAPIView):
    # This endpoint will delete the todo list by passing id in the url
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
