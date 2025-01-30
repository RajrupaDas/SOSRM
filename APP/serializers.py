from rest_framework import serializers
from .models import CustomUser, Image, SecureWay, SOS, Buddy

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'  # Include all fields

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class SecureWaySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)  # Nested image details

    class Meta:
        model = SecureWay
        fields = '__all__'

class SOSSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = SOS
        fields = '__all__'

class BuddySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Buddy
        fields = '__all__'

