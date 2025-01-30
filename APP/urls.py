from django.urls import path, include
from .views import register, user_login, sos, secureway, find_buddies, index
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ImageViewSet, SecureWayViewSet, SOSViewSet, BuddyViewSet
from . import views

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'images', ImageViewSet)
router.register(r'secureway', SecureWayViewSet)
router.register(r'sos', SOSViewSet)
router.register(r'buddy', BuddyViewSet)

urlpatterns = [
    path("register/", register),
    path('', index, name='index'),
    path("login/", user_login),
    path("sos/", sos),
    path("secureway/<str:category>/", secureway),
    path("find_buddies/", find_buddies),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

