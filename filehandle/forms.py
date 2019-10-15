from django import forms
from .models import Photo
#DataFlair #File_Upload
class Photo_Form(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['display',]
