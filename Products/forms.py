from django import forms
from .models import Sale
from django.forms import ModelForm, TextInput
from cloudinary.forms import CloudinaryFileField


class StartSale(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['Title', 'Sale_Img']

    Sale_Img = CloudinaryFileField(
        options={
            'folder': 'DNF/',
            'resource_type': 'auto',
        })

    def __init__(self, *args, **kwargs):
        super(StartSale, self).__init__(*args, **kwargs)
