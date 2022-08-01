from email.policy import default
from pydoc import describe
from statistics import mode
from tkinter import CASCADE
import uuid
from django.db import models
from users.models import Profile

class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    describe = models.TextField(null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, default='default.jpg')
    vote_total = models.IntegerField(default=0, null=True , blank=True)
    tag = models.ManyToManyField('Tag', blank=True)
    vote_ratio = models.IntegerField(default=0, null=True , blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4 , primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.title

class vote(models.Model):
    vote = (
        ('up', 'upvote'),
        ('down', 'downvote')
    )
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.CharField(null=True, max_length=200)
    value = models.CharField(choices=vote, max_length=200)
    id = models.UUIDField(default = uuid.uuid4 , primary_key=True, unique=True, editable=False)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name