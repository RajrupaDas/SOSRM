from django.contrib import admin

# Register your models here.

from .models import CustomUser, SecureWay, SOS, Buddy, Image

# Register models to Django admin
admin.site.register(CustomUser)
admin.site.register(SecureWay)
admin.site.register(SOS)
admin.site.register(Buddy)
admin.site.register(Image)
