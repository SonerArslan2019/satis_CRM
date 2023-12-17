from django.shortcuts import render, redirect
from django.http import HttpResponse


def teklif_olustur(request):
    # Burada teklif oluşturma işlemleri yapılacak
    return HttpResponse("Teklif başarıyla oluşturuldu.")


def fatura_olustur(request):
    # Burada fatura oluşturma işlemleri yapılacak
    return HttpResponse("Fatura başarıyla oluşturuldu.")


def kaydi_duzenle(request, id):
    # Burada mevcut müşteri kaydını düzenleme işlemleri yapılacak
    # Örnek olarak 'id' parametresi kullanılıyor
    return HttpResponse(f"Müşteri kaydı {id} numarası ile düzenlendi.")


def kaydi_sil(request, id):
    # Burada mevcut müşteri kaydını silme işlemleri yapılacak
    # Örnek olarak 'id' parametresi kullanılıyor
    return HttpResponse(f"Müşteri kaydı {id} numarası ile silindi.")


def yeni_musteri(request):
    # Burada yeni müşteri kaydı oluşturma işlemleri yapılacak
    return render(request, 'yenimusteri_sayfasi.html')
