from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    InstitucionViewSet,
    RepresentanteViewSet,
    CarreraOfertadaViewSet,
    SedeViewSet,
)

router = DefaultRouter()
router.register(r"instituciones", InstitucionViewSet)
router.register(r"representantes", RepresentanteViewSet)
router.register(r"carreras", CarreraOfertadaViewSet)
router.register(r"sedes", SedeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
