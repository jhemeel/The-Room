from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(default=18, null=True, blank=True)
    gender = models.Choices('Male', 'Female')
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to='profile-pic', default='empty-profile.png')
    location = models.CharField(max_length=100, blank=True, null=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name_plural = 'User'
        
        
class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'Topic'
    
    
    def __str__(self):
        return self.name
    
class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, unique=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['-updated_at', '-created_at']
        verbose_name_plural = 'Room'
        
     
    def __str__(self):
        return self.name
    
    

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    no_of_likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at', '-created_at']
        verbose_name_plural = 'Message'
        
     
    def __str__(self):
        return self.body[0:50]
    
    
    