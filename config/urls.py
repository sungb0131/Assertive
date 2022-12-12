from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "보금자리 관리자"

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('baton/', include('baton.urls')),
    path('main/', include('main.urls')),
    path('', include('common.urls'))
]
