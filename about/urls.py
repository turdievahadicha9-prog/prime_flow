from django.urls import path
from .views import AboutAPIView, about_page


urlpatterns = [
    path('about/', AboutAPIView.as_view(), name='about-api'),
    path('page/', about_page, name='about-page'),
]