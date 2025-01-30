from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import AbstractUser, Group, Permission

@receiver(post_save, sender=CustomUser)
def send_verification_email(sender, instance, created, **kwargs):
    if created:
        token = default_token_generator.make_token(instance)
        uid = urlsafe_base64_encode(str(instance.pk).encode())
        
        # Build the URL for verification
        verification_url = f"http://{get_current_site(None).domain}/verify-email/{uid}/{token}/"
        
        message = render_to_string('account/verification_email.html', {
            'user': instance,
            'verification_url': verification_url,
        })
        
        send_mail('Verify Your Email', message, 'noreply@yourapp.com', [instance.email])

class CustomUser(AbstractUser):
    id_number = models.CharField(max_length=10, unique=True)
    location = models.CharField(max_length=5, unique=True)

    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    def save(self, *args, **kwargs):
        if not self.location and not self.pk:  # Ensure pk exists before using it
            super().save(*args, **kwargs)  # Save first to get a pk
            self.location = str(10000 + self.pk % 90000)  # Generate unique 5-digit location
        super().save(*args, **kwargs)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')

class SecureWay(models.Model):
    category = models.CharField(max_length=20, unique=True)  # "Students", "Staff", "Security"
    images = models.ManyToManyField(Image, related_name="secureway_images") # Stores images

class SOS(models.Model):
    phone_number = models.CharField(max_length=15)  # Stores the emergency phone number
    images = models.ManyToManyField(Image, related_name="sos_images")  # Stores the SOS image

class Buddy(models.Model):
    images = models.ManyToManyField(Image, related_name="buddy_images")
