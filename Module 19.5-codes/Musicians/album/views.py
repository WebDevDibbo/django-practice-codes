from django.views.generic import CreateView,UpdateView,DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from . import forms

# Create your views here.
class AddAlbum(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')

    def form_valid(self, form):
        form.instance.Musician = self.request.user
        return super().form_valid(form)
    
class EditAlbum(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

class DeleteMusician(DeleteView):
    model = models.Album
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    