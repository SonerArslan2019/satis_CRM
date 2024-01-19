from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import FirmaForm, TeklifForm, FaturaForm
from .models import Firma, Teklif, Fatura


@login_required
def musteri_goruntule(request, id):
    musteri = get_object_or_404(Firma, id=id)
    return render(request, 'musteri_goruntule.html', {'musteri': musteri})


@login_required
def yeni_musteri_olustur(request):
    if request.method == "POST":
        form = FirmaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Form başarıyla oluşturuldu")
            return HttpResponseRedirect(reverse('satis:yeni_musteri_olustur'))
        else:
            return render(request, "yeni_musteri_olustur.html", {'form': form})
    else:
        form = FirmaForm()
        return render(request, "yeni_musteri_olustur.html", {'form': form})


@login_required
def musteri_listele(request):
    # Global search
    if 'q' in request.GET:
        q = request.GET['q']
        kayitlar = Firma.objects.filter(
            Q(firma_adi__icontains=q) | Q(yetkili_adi__icontains=q) | Q(telefon_no__icontains=q)).order_by('-id')
    else:
        kayitlar = Firma.objects.all().order_by('-id')
    # pagination
    paginator = Paginator(kayitlar, 10)
    page = request.GET.get('page')
    kayitlar = paginator.get_page(page)
    context = {'kayitlar': kayitlar}
    return render(request, "musteri_listele.html", context)


@login_required
def teklif_olustur(request, firma_id):
    firma = get_object_or_404(Firma, id=firma_id)
    if request.method == 'POST':
        form = TeklifForm(request.POST)
        if form.is_valid():
            teklif = form.save(commit=False)
            teklif.firma = firma
            teklif.save()
            messages.success(request, "Teklif başarıyla oluşturuldu.")
            return redirect('satis:teklif_listesi', firma_id=firma_id)
    else:
        form = TeklifForm()
    return render(request, 'teklif_olustur.html', {'form': form, 'firma_id': firma_id})


@login_required
def fatura_olustur(request, firma_id):
    firma = get_object_or_404(Firma, id=firma_id)
    if request.method == 'POST':
        form = FaturaForm(request.POST)
        if form.is_valid():
            fatura = form.save(commit=False)
            fatura.firma = firma
            fatura.save()
            messages.success(request, "Fatura başarıyla oluşturuldu.")
            return redirect('satis:fatura_listesi')
    else:
        form = FaturaForm()
    return render(request, 'fatura_olustur.html', {'form': form, 'firma': firma})


@login_required
def kayit_degistir(request, id):
    firma = get_object_or_404(Firma, id=id)
    if request.method == 'POST':
        form = FirmaForm(request.POST, instance=firma)
        if form.is_valid():
            form.save()
            messages.success(request, "Firma kaydı başarıyla güncellendi.")
            return redirect('satis:musteri_listele')
    else:
        form = FirmaForm(instance=firma)
    return render(request, 'firma_form.html', {'form': form})


@login_required
def kayit_sil(request, id):
    firma = get_object_or_404(Firma, id=id)
    firma.delete()
    messages.success(request, "Firma kaydı başarıyla silindi.")
    return redirect('satis:musteri_listele')


@login_required
def teklif_listesi(request, firma_id):
    teklifler = Teklif.objects.filter(firma_id=firma_id).order_by('-olusturma_tarihi')
    return render(request, 'teklif_listesi.html', {'teklifler': teklifler})



@login_required
def fatura_listesi(request):
    faturalar = Fatura.objects.all().order_by('-fatura_tarihi')
    return render(request, 'fatura_listesi.html', {'faturalar': faturalar})
