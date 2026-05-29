from django.contrib import admin
from django.urls import path
from .views import PerfilTreinadorView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "api/treinador/perfil/", PerfilTreinadorView.as_view(), name="perfil_treinador"
    ),
]
