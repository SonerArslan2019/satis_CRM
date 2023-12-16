from django.shortcuts import render, redirect


def satis_ilksayfa(request):
    if request.user.is_authenticated:
        return redirect('home:satis_homepage')
    return render(request, 'home.html')


def satis_homepage(request):
    return render(request, 'satis_homepage.html')


def fatura_sayfasi(request):
    return render(request, "../templates/fatura_sayfasi.html")


def kontaklar_sayfasi(request):
    return render(request, "../templates/kontaklar_sayfasi.html")


def teklif_sayfasi(request):
    return render(request, "../templates/teklif_sayfasi.html")


def view_401(request):
    return render(request, '401.html', {})
