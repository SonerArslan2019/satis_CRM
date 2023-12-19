from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import FirmaForm
from .models import Firma



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
    paginator = Paginator(kayitlar, 7)
    page = request.GET.get('page')
    kayitlar = paginator.get_page(page)
    context = {'kayitlar': kayitlar}
    return render(request, "musteri_listele.html", context)
