from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'myapp.views.error404'

urlpatterns = [
    path('olx/', include('olx.urls')),   # include app URLs
    path('admin/', admin.site.urls),
]

# During local development we still want static files served when DEBUG=False
# so the custom 404 page can be tested. This mounts the app static directory.
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=str(settings.BASE_DIR / 'olx' / 'static'))
