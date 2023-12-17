from django.urls import path

from .views import *

app_name = "home"

urlpatterns = [
    path('', satis_ilksayfa, name='satis_ilksayfa'),
    path('satis_homepage/', satis_homepage, name='satis_homepage'),
    path('yenimusteri_sayfasi/', yenimusteri_sayfasi, name='yenimusteri_sayfasi'),
    path('401/', view_401, name='401'),
]
