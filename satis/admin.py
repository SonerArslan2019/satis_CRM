from django.contrib import admin
from .models import Firma, Teklif, Fatura


@admin.register(Firma)
class FirmaAdmin(admin.ModelAdmin):
    list_display = ('firma_adi', 'yetkili_adi', 'telefon_no', 'email')
    search_fields = ('firma_adi', 'yetkili_adi', 'email')
    list_filter = ('firma_adi',)
    ordering = ('firma_adi',)
    fields = ('firma_adi', 'yetkili_adi', 'adres', 'telefon_no', 'fax', 'email')


@admin.register(Teklif)
class TeklifAdmin(admin.ModelAdmin):
    list_display = ('teklif_adi', 'firma', 'olusturma_tarihi', 'son_gecerlilik_tarihi')
    search_fields = ('teklif_adi', 'firma__firma_adi')
    list_filter = ('firma', 'olusturma_tarihi')
    ordering = ('-olusturma_tarihi',)
    fields = ('firma', 'teklif_adi', 'olusturma_tarihi', 'son_gecerlilik_tarihi', 'detaylar')
    raw_id_fields = ('firma',)


@admin.register(Fatura)
class FaturaAdmin(admin.ModelAdmin):
    list_display = ('fatura_adi', 'firma', 'fatura_tarihi', 'odeme_tarihi', 'tutar')
    search_fields = ('fatura_adi', 'firma__firma_adi')
    list_filter = ('firma', 'fatura_tarihi')
    ordering = ('-fatura_tarihi',)
    fields = ('firma', 'fatura_adi', 'fatura_tarihi', 'odeme_tarihi', 'tutar', 'aciklama')
    raw_id_fields = ('firma',)
