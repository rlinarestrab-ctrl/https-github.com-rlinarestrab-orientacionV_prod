from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserViewSet
from .auth import login_view, register_view
from .auth import login_view, register_view, logout_view 

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("auth/login/", login_view),
    path("auth/register/", register_view),
    path("auth/refresh/", TokenRefreshView.as_view()),
    path("auth/logout/", logout_view),
    path("", include(router.urls)),
]
