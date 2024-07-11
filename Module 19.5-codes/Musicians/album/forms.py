from django import forms
from album.models import Album
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            forms.TextInput(attrs={'placeholder':'Enter your Album name '})
        }