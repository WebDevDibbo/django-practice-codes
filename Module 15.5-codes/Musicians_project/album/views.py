from django.shortcuts import render,redirect
from album.forms import AlbumForm
from .  import models
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form = AlbumForm()
    return render(request,'album_form.html',{'form':album_form})

def edit_album(request,id):
    album = models.Album.objects.get(pk=id)
    album_form = AlbumForm(instance=album)
    if request.method == 'POST':
        album_form = AlbumForm(request.POST,instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    return render(request,'album_form.html',{'form':album_form})

def delete_musician(request,id):
    musician = models.Album.objects.get(pk=id)
    musician.delete()
    return redirect('home')