from django.shortcuts import render
from first_app.forms import ContactForm, userForm

# Create your views here.
def home(request):
    return render(request,'first_app/home.html')

def djangoForm(request):
    if request.method == 'POST':
        form  = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ContactForm()
    return render(request,'first_app/django_form.html',{'form': form})

def modelForm(request):
    if request.method == 'POST':
        user_form  = userForm(request.POST)
        if user_form.is_valid():
            print(user_form.cleaned_data)
    else:
        user_form = userForm()
    return render(request,'first_app/model_form.html',{'form': user_form})