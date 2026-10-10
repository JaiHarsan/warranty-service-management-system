
from django.urls import path, include, re_path
from django.views.static import serve
import os
from django.conf import settings

FRONTEND_DIR = os.path.join(settings.BASE_DIR.parent, 'frontend')

urlpatterns = [
    path('api/', include('apps.accounts.urls')),
    path('api/', include('apps.products.urls')),
    path('api/', include('apps.warranties.urls')),
    path('api/', include('apps.health_checks.urls')),
    path('api/', include('apps.service_centres.urls')),
    path('api/', include('apps.appointments.urls')),
    path('api/', include('apps.documents.urls')),
    path('api/', include('apps.notifications.urls')),
    path('api/', include('apps.service_history.urls')),
    path('', serve, {'document_root': FRONTEND_DIR, 'path': 'index.html'}),
    re_path(r'^(?P<path>.*)$', serve, {'document_root': FRONTEND_DIR}),
]
