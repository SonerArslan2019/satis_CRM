from django.urls import path
from . import views

app_name = "satis"

urlpatterns = [
    path('musteri_goruntule/<id>', views.musteri_goruntule, name='musteri_goruntule'),
    path('yeni_musteri_olustur/', views.yeni_musteri_olustur, name='yeni_musteri_olustur'),
    path('musteri_listele/', views.musteri_listele, name='musteri_listele'),
    # Diğer URL desenleri...
]
