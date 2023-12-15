from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('', include("home", namespace='home')),
                  path('user/', include("user", namespace='user')),
                  path('fatura/', include("fatura", namespace='fatura')),
                  path('kontaklar/', include("kontaklar", namespace='kontaklar')),
                  path('teklif/', include("teklif", namespace='teklif')),
                  path('admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
