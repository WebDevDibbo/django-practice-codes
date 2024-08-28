from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class RegistrationForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'id':'required'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class EditUserProfile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

    def __init__(self, *args, **kwargs):
        super(EditUserProfile, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['disabled'] = 'disabled'
        self.fields['first_name'].widget.attrs['disabled'] = 'disabled'
        self.fields['last_name'].widget.attrs['disabled'] = 'disabled'
        self.fields['email'].widget.attrs['disabled'] = 'disabled'


