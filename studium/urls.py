from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("auth/", include("auth.urls")),
    path("grades/", include("grades.urls")),
    path("admin/", admin.site.urls),
]
