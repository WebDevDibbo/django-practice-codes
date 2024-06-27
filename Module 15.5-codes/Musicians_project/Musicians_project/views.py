from django.shortcuts import render
from musician.models import Musician
from album.models import Album
def home(request):
    data = Album.objects.all()
    return render(request,'home.html',{'data': data})