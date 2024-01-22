from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('', include(("user.urls", "user"), namespace='user_home')),
                  path('user/', include(("user.urls", "user"), namespace='user')),
                  path('satis/', include(("satis.urls", "satis"), namespace='satis')),
                  path('admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
