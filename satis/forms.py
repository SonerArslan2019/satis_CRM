from django import forms
from django.core.exceptions import ValidationError

from .models import Firma, Teklif, Fatura


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

    def clean_firma_adi(self):
        firma_adi = self.cleaned_data.get('firma_adi')
        if Firma.objects.filter(firma_adi=firma_adi).exists():
            raise ValidationError("Bu firma adı zaten kullanımda. Lütfen farklı bir isim deneyin.")
        return firma_adi


class TeklifForm(forms.ModelForm):
    class Meta:
        model = Teklif
        fields = ['teklif_adi', 'son_gecerlilik_tarihi', 'detaylar']


class FaturaForm(forms.ModelForm):
    class Meta:
        model = Fatura
        fields = ['fatura_adi', 'fatura_tarihi', 'odeme_tarihi', 'tutar', 'aciklama']
