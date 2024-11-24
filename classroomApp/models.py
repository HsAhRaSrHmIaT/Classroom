from django.db import models #type: ignore
from django.contrib.auth.models import User #type: ignore
from django.db.models.signals import post_save #type: ignore
from django.dispatch import receiver #type: ignore
from PIL import Image
import os

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Room(models.Model):
    host= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[:50]
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', default=None, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    github = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True)
    
    # Additional fields that might be useful
    location = models.CharField(max_length=100, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        # Call the parent save method
        super().save(*args, **kwargs)

        # Process the avatar image if one exists
        if self.avatar and hasattr(self.avatar, 'path') and os.path.exists(self.avatar.path):
            img = Image.open(self.avatar.path)
            
            # Resize image if it's too large
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.avatar.path)

# Signal to create/update profile when user is created/updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        Profile.objects.get_or_create(user=instance)