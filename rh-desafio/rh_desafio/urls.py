import patterns as patterns
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve
from core.views import pagina_inicial


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
