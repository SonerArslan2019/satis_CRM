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
