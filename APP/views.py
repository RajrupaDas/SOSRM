from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import CustomUser, SecureWay, SOS, Buddy
from rest_framework import viewsets
from .models import CustomUser, Image, SecureWay, SOS, Buddy
from .serializers import CustomUserSerializer, ImageSerializer, SecureWaySerializer, SOSSerializer, BuddySerializer

def verify_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            message = "Your email has been verified successfully!"
        else:
            message = "The verification link is invalid or expired."
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        message = "Invalid verification link."
    
    return render(request, 'account/verification_confirmation.html', {'message': message})

def index(request):
    secureways = SecureWay.objects.all()
    sos_list = SOS.objects.all()
    return render(request, 'APP/index.html', {'secureways': secureways, 'sos_list': sos_list})

@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        id_number = data.get("id_number")
        password = data.get("password")

        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({"error": "User already exists"}, status=400)

        user = CustomUser.objects.create_user(email=email, id_number=id_number, password=password, username=email)
        return JsonResponse({"message": "User created", "location": user.location})

@csrf_exempt
def user_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return JsonResponse({"message": "Login successful", "location": user.location})
        return JsonResponse({"error": "Invalid credentials"}, status=400)

@csrf_exempt
def sos(request):
    sos_entry = SOS.objects.first()
    if sos_entry:
        return JsonResponse({
            "phone_number": sos_entry.phone_number,
            "images": [image.image.url for image in sos_entry.images.all()]
        })
    return JsonResponse({"error": "No SOS entry found"}, status=400)



@csrf_exempt
def secureway(request, category):
    secureway_entry = SecureWay.objects.filter(category=category).first()
    if secureway_entry:
        return JsonResponse({
            "images": [image.image.url for image in secureway_entry.images.all()]
        })
    return JsonResponse({"error": "Category not found"}, status=400)



@csrf_exempt
def find_buddies(request):
     if request.method == "POST":
        data = json.loads(request.body)
        location = data.get("location")

        buddies = CustomUser.objects.filter(location__startswith=location[0]).values_list("email", flat=True)
        buddy_images = Buddy.objects.first()

        return JsonResponse({
            "buddies": list(buddies),
            "images": [image.image.url for image in buddy_images.images.all()] if buddy_images else []
        })

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class SecureWayViewSet(viewsets.ModelViewSet):
    queryset = SecureWay.objects.all()
    serializer_class = SecureWaySerializer

class SOSViewSet(viewsets.ModelViewSet):
    queryset = SOS.objects.all()
    serializer_class = SOSSerializer

class BuddyViewSet(viewsets.ModelViewSet):
    queryset = Buddy.objects.all()
    serializer_class = BuddySerializer
