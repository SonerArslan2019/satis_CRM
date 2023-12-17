from django.urls import path
from . import views

app_name = "satis"


urlpatterns = [
    path('teklif-olustur/', views.teklif_olustur, name='teklif_olustur'),
    path('fatura-olustur/', views.fatura_olustur, name='fatura_olustur'),
    path('kaydi-duzenle/<int:id>/', views.kaydi_duzenle, name='kaydi_duzenle'),
    path('kaydi-sil/<int:id>/', views.kaydi_sil, name='kaydi_sil'),
    path('yeni-musteri/', views.yeni_musteri, name='yeni_musteri'),
    # Diğer URL desenleri...
]

