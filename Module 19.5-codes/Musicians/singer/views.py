
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from . import forms
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully')
            return redirect('home')
    else:
        form = forms.RegistrationForm()
    return render(request, 'register.html', {'form':form,'type' : 'Register'})


class UserLogin(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self,form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.success(self.request, 'information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
class logout(LogoutView):
    next_page = 'home'