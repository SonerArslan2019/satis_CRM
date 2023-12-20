from django.urls import path
from .views import musteri_goruntule, yeni_musteri_olustur, musteri_listele, teklif_olustur, fatura_olustur, \
    kayit_degistir, kayit_sil, teklif_listesi, fatura_listesi

app_name = "satis"

urlpatterns = [
    path('musteri_goruntule/<id>', musteri_goruntule, name='musteri_goruntule'),
    path('yeni_musteri_olustur/', yeni_musteri_olustur, name='yeni_musteri_olustur'),
    path('musteri_listele/', musteri_listele, name='musteri_listele'),
    path('teklif_olustur/<int:firma_id>/', teklif_olustur, name='teklif_olustur'),
    path('fatura_olustur/<int:firma_id>/', fatura_olustur, name='fatura_olustur'),
    path('kayit_degistir/<int:id>/', kayit_degistir, name='kayit_degistir'),
    path('kayit_sil/<int:id>/', kayit_sil, name='kayit_sil'),
    path('teklif_listesi/', teklif_listesi, name='teklif_listesi'),
    path('fatura_listesi/', fatura_listesi, name='fatura_listesi'),
    # Diğer URL desenleri...
]
