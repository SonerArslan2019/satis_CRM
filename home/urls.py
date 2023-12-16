from django.urls import path

from .views import *

app_name = "home"

urlpatterns = [
    path('', satis_ilksayfa, name='satis_ilksayfa'),
    path('satis_homepage/', satis_homepage, name='satis_homepage'),
    path('fatura_sayfasi/', fatura_sayfasi, name='fatura_sayfasi'),
    path('kontaklar_sayfasi/', kontaklar_sayfasi, name='kontaklar_sayfasi'),
    path('teklif_sayfasi/', teklif_sayfasi, name='teklif_sayfasi'),
    path('401/', view_401, name='401'),
]
