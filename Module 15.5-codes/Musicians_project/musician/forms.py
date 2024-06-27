from django import forms
from musician.models import Musician
class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
        widgets = {
            'First_name' : forms.TextInput(attrs={'placeholder' : "Enter your first Name "}),
            'last_name' : forms.TextInput(attrs={'placeholder' : "Enter your last Name "}),
            'Phone_number' : forms.TextInput(attrs={'placeholder' : "Enter your Phone Number "}),
            'Email' : forms.TextInput(attrs={'placeholder' : "Enter your Email "}),
        }
