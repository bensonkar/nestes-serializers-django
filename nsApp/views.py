from django.shortcuts import render
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.serializers import Serializer

from nsApp.models import Book
from .models import Author,Book
from rest_framework import generics
from nsApp.Serializer import AuthorSerializer,BookSerializer


# Create your views here.
class AuthorListView(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer    

class BookListView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer    