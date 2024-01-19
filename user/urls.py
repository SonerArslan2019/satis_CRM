from django.urls import path
from .views import login_view, logout_view

app_name = "user"

urlpatterns = [
    path('', login_view, name='login_view'),
    path('cikis/', logout_view, name="logout"),
]
