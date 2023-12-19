from django.urls import path

from .views import *

app_name = "home"

urlpatterns = [
    path('', satis_ilksayfa, name='satis_ilksayfa'),
    path('401/', view_401, name='401'),
]
