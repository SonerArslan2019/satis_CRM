from django.db import models


class Firma(models.Model):
    firma_adi = models.CharField(max_length=200, verbose_name="Firma Adı")
    yetkili_adi = models.CharField(max_length=100, verbose_name="Yetkili Adı")
    adres = models.TextField(verbose_name="Adres")
    telefon_no = models.CharField(max_length=15, verbose_name="Telefon Numarası")
    fax = models.CharField(max_length=15, verbose_name="Faks", blank=True, null=True)
    email = models.EmailField(verbose_name="E-Mail Adresi")

    def __str__(self):
        return self.firma_adi


class Teklif(models.Model):
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE, related_name='teklifler')
    teklif_adi = models.CharField(max_length=200)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    son_gecerlilik_tarihi = models.DateField()
    detaylar = models.TextField()

    def __str__(self):
        return f"{self.teklif_adi} - {self.firma.firma_adi}"


class Fatura(models.Model):
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE, related_name='faturalar')
    fatura_adi = models.CharField(max_length=200)
    fatura_tarihi = models.DateField(null=True, blank=True)
    odeme_tarihi = models.DateField(null=True, blank=True)
    tutar = models.DecimalField(max_digits=10, decimal_places=2)
    aciklama = models.TextField()

    def __str__(self):
        return f"{self.fatura_adi} - {self.firma.firma_adi}"
