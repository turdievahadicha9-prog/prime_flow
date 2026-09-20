from rest_framework.views import APIView
from rest_framework.response import Response
from .models import About
from .serializers import AboutSerializer
from django.shortcuts import render


class AboutAPIView(APIView):
    def get(self, request):
        about = About.objects.first()
        serializer = AboutSerializer(about)
        return Response(serializer.data)


def about_page(request):
    return render(request, 'about/index.html')