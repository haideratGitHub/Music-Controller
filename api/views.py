from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
# def main(request):
#     return HttpResponse("<h1>Hello<h1>")

# Adding API endpoint/view which will be used to fetch data in json from db
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer