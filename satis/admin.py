from django.contrib import admin
from .models import Firma


@admin.register(Firma)
class FirmaAdmin(admin.ModelAdmin):
    list_display = ('firma_adi', 'yetkili_adi', 'telefon_no', 'email')
    search_fields = ('firma_adi', 'yetkili_adi', 'email')
    list_filter = ('firma_adi',)
    ordering = ('firma_adi',)
    fields = ('firma_adi', 'yetkili_adi', 'adres', 'telefon_no', 'fax', 'email')
