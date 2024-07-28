from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("run/", include("postpilot.urls")),
    path('user/', include('django.contrib.auth.urls')),
    path('user/', include('user.urls')),
    path('accounts/', include('allauth.urls')),
]
