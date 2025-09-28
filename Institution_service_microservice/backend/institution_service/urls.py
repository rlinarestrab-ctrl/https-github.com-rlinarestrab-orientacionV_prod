from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),        # 👈 registra el admin
    path("api/", include("institutions.urls")),
]
