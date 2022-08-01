import uuid
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
class Profile(models.Model):
    user = models.OneToOneField(
        User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True , null= True)
    email = models.EmailField(max_length=500, blank=True , null= True)
    username = models.CharField(max_length=200, blank=True , null= True)
    location = models.CharField(max_length=200, blank=True , null= True)
    short_intro = models.CharField(max_length=200, blank=True, null= True)
    bio = models.TextField(blank=True, null=True)
    profile_img = models.ImageField(null = True, blank= True, upload_to = 'profile/', default = 'profile/user-default.png')
    social_github = models.CharField(max_length=200, blank=True , null= True)
    social_linkedin = models.CharField(max_length=200, blank=True , null= True)
    social_youtube = models.CharField(max_length=200, blank=True , null= True)
    social_twitter = models.CharField(max_length=200, blank=True , null= True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self):
        return str(self.user.username)

class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4 , primary_key=True, unique=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    descreption = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)

def createprofile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            name = user.first_name,
            email = user.email,
    )

def edituser(sender , instance, created , **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

def deleteuser(sender, instance, **Kwargs):
    print('Deleting User...')

post_save.connect(edituser, sender=Profile)

post_save.connect(createprofile, sender=User)