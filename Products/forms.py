from django import forms
from .models import Sale, Product, ProdImg, Company
from django.forms import ModelForm, TextInput
from cloudinary.forms import CloudinaryFileField


class StartSale(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['Title', 'Sale_Img']

    Sale_Img = CloudinaryFileField(
        options={
            'folder': 'DNF/Sales/',
            'resource_type': 'image',
        }
    )

    def __init__(self, *args, **kwargs):
        super(StartSale, self).__init__(*args, **kwargs)


class AddProd(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Comp', 'Name', 'Price', 'Stock', 'Dscrp']

    def __init__(self, *args, **kwargs):
        super(AddProd, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'validate'
            field.widget.attrs['style'] = 'color: white;'

        self.fields['Dscrp'].widget.attrs['class'] = 'materialize-textarea'


class PdIgFrm(forms.ModelForm):
    class Meta:
        model = ProdImg
        fields = ['Sno', 'Img', ]

    Img = CloudinaryFileField(
        options={
            'folder': 'DNF/Products/',
            'resource_type': 'image',
        }
    )

    def __init__(self, *args, **kwargs):
        super(PdIgFrm, self).__init__(*args, *kwargs)
