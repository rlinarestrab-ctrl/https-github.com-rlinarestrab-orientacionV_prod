from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),          # opcional pero útil
    path("api/", include("users.urls")),      # expone /api/...
]
