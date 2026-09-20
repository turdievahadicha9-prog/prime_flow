import requests

from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import generics, permissions, viewsets

from .models import Flower, Order
from .serializers import FlowerSerializer, RegisterSerializer
from .forms import OrderForm


def send_telegram(text):
    """
    Отправка сообщения в Telegram
    """
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": settings.TELEGRAM_CHAT_ID,
            "text": text,
        },
    )


def home(request):
    flowers = Flower.objects.all()

    return render(
        request,
        "flower/base.html",
        {
            "flowers": flowers,
        },
    )


def order_flower(request, pk):
    """
    Оформление заказа
    """

    flower = get_object_or_404(Flower, pk=pk)

    if request.method == "POST":

        form = OrderForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)
            order.flower = flower
            order.save()

            message = (
                "🌸 Новый заказ!\n\n"
                f"🌷 Цветок: {flower.name}\n\n"
                f"👤 Заказчик: {order.customer_name}\n"
                f"🎁 Получатель: {order.receiver_name}\n"
                f"📞 Телефон: {order.phone}\n"
                f"📍 Адрес:\n{order.address}"
            )

            send_telegram(message)

            return redirect("home")

    else:
        form = OrderForm()

    return render(
        request,
        "flower/order.html",
        {
            "form": form,
            "flower": flower,
        },
    )


class FlowerViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer

    def get_permissions(self):
        # Просматривать каталог могут все
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]

        # Создавать, изменять и удалять только авторизованные
        return [permissions.IsAuthenticated()]


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]