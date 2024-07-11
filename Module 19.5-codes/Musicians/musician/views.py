
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from . import models
from . import forms

# Create your views here.

class AddMusician(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')
    def form_valid(self,form):
        self.object = form.save()
        return super().form_valid(form)
