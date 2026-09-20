from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    FlowerViewSet,
    RegisterView,
    home,
    order_flower,
)

router = DefaultRouter()
router.register(
    "flowers",
    FlowerViewSet,
    basename="flower",
)

urlpatterns = [
    # Главная страница
    path("", home, name="home"),

    # Страница оформления заказа
    path(
        "order/<int:pk>/",
        order_flower,
        name="order_flower",
    ),

    # API
    path("api/", include(router.urls)),

    # Регистрация
    path(
        "api/register/",
        RegisterView.as_view(),
        name="register",
    ),
]