from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("api/user/", include("user.urls", namespace="user")),
    path("api/", include("analytic.urls")),
]
