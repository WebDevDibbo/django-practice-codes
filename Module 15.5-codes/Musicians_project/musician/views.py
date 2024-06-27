from django.shortcuts import render,redirect
from musician.forms import MusicianForm
from . import models
# Create your views here.
def addMusician(request):
    if request.method == 'POST':
        musician_form = MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    else:
        musician_form = MusicianForm()
    return render(request,'musician_form.html',{'form':musician_form})

def editMusician(request,id):
    musician = models.Musician.objects.get(pk=id)
    musician_form = MusicianForm(instance=musician)
    if request.method == 'POST':
        musician_form = MusicianForm(request.POST,instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
    return render(request,'musician_form.html',{'form':musician_form})

