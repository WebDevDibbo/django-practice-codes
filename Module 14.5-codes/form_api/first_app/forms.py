from django import forms
from first_app.models import MyModel
import datetime

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
FAVORITE_FRUIT_CHOICES = [
    ('orange', 'Orange'),
    ('apple', 'Apple'),
    ('mango', 'Mango'),
]


class ContactForm(forms.Form):
    name = forms.CharField(label='Please enter your Full Name',initial='Your name')
    email = forms.EmailField(label="Please enter your email address")
    agree = forms.BooleanField()
    date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    roll_number = forms.IntegerField( help_text = "Enter 6 digit roll number") 
    # birth_year = forms.DateField(widget=forms.SelectDateWidget)
    value = forms.DecimalField()
    message = forms.CharField()
    # comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    fruit = forms.MultipleChoiceField(choices=FAVORITE_FRUIT_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    


class userForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'
    