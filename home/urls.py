from django.urls import path

from .views import *

app_name = "home"

urlpatterns = [
    path('', ilksayfa, name='ilksayfa'),
    path('imalat_homepage/', imalat_homepage, name='imalat_homepage'),
    path('mr30_isemri_kapilar/', mr30_isemri_kapilar, name='mr30_isemri_kapilar'),
    path('mr30_isemriolustur/', mr30_isemriolustur, name='mr30_isemriolustur'),
    path('401/', view_401, name='401'),
]
