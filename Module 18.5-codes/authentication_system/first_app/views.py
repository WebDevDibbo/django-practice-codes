from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import RegistrationForm , EditUserProfile

# Create your views here.
def home(request):
    return render(request, 'home.html')

def SignUp(request):
    # if request.user.is_authenticated:
    if request.method == 'POST':
        signup_form = RegistrationForm(request.POST)
        if signup_form.is_valid():
            messages.success(request,'Account Created Successfully')
            signup_form.save()
            redirect('home')
    else:
        signup_form = RegistrationForm()
    return render(request, 'signup.html', {'form' : signup_form})




def LogIn(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request = request, data = request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully')
                return redirect('profile')
            else:
                messages.warning(request, 'Invalid username or password')
        else:
            messages.warning(request, 'Invalid username or password')
            
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'form': login_form})


def Profile(request):
    if request.user.is_authenticated:
        form = EditUserProfile(instance = request.user)
        return render(request, 'profile.html', {'form':form})
    else:
        return redirect('signup')



def changePass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pass_form = PasswordChangeForm(user=request.user, data = request.POST)
            if pass_form.is_valid():
                messages.success(request, 'Password Changed Successfully')
                pass_form.save()
                update_session_auth_hash(request, pass_form.user)
                return redirect('profile')
        else:
            pass_form = PasswordChangeForm(request.user)
        return render(request, 'change_pass.html', {'form':pass_form})
    else:
        return redirect('login')
    


def setPass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pass_form = SetPasswordForm(user=request.user, data = request.POST)
            if pass_form.is_valid():
                messages.success(request, 'Password Changed Successfully')
                pass_form.save()
                update_session_auth_hash(request, pass_form.user)
                return redirect('profile')
        else:
            pass_form = SetPasswordForm(request.user)
        return render(request, 'change_pass.html', {'form':pass_form})
    else:
        return redirect('login')



def LogOut(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('home')
