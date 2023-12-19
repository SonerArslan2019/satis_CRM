from django import forms
from .models import Firma


class FirmaForm(forms.ModelForm):
    class Meta:
        model = Firma
        fields = ['firma_adi', 'yetkili_adi', 'adres', 'telefon_no', 'fax', 'email']
        labels = {
            'firma_adi': 'Firma Adı',
            'yetkili_adi': 'Yetkili Adı',
            'adres': 'Adres',
            'telefon_no': 'Telefon Numarası',
            'fax': 'Faks',
            'email': 'E-mail Adresi'
        }
        widgets = {
            'firma_adi': forms.TextInput(attrs={'class': 'form-control'}),
            'yetkili_adi': forms.TextInput(attrs={'class': 'form-control'}),
            'adres': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'telefon_no': forms.TextInput(attrs={'class': 'form-control'}),
            'fax': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }
