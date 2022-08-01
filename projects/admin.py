from atexit import register
from django.contrib import admin
from .models import Project, vote , Tag

admin.site.register(Project)
admin.site.register(vote)
admin.site.register(Tag)