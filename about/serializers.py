from rest_framework import serializers
from .models import About, Advantage, Gallery


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    advantages = serializers.SerializerMethodField()
    gallery = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = '__all__'

    def get_advantages(self, obj):
        return AdvantageSerializer(
            Advantage.objects.all(),
            many=True
        ).data

    def get_gallery(self, obj):
        return GallerySerializer(
            Gallery.objects.all(),
            many=True
        ).data