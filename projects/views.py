from unittest import result
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from projects.forms import projectform
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Project, Tag


data = [

    {
    'id': '1',
    'name': 'Fahad Asad',
    'Des': 'This is fahad asad from 8th sem'
    },
    {
    'id': '2',
    'name': 'Mula Yakoob',
    'Des': 'This is Mulla Yakoob from idk where'
    },
    {
    'id': '3',
    'name': 'Arbab Malik',
    'Des': 'This is Arbab Malik from Security systems'
    },
]


def projects(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tag = Tag.objects.filter(name__icontains=search_query)
    obj = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(describe__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tag__in=tag)
        )
    page = request.GET.get('page')
    results = 2
    paginator= Paginator(obj, results)
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        obj = paginator.page(page)

    return render(request, 'projects/projects.html',{'list': obj})

def project(request, pk):
    obj = Project.objects.get(id = pk)
    tags = obj.tag.all()
    return render(request, 'projects/project.html', {'list': obj, 'tags': tags})


@login_required(login_url='login')
def create_project(request):
    profile = request.user.profile
    form = projectform
    if request.method == 'POST':
        form = projectform(request.POST, request.FILES)
        if form.is_valid:
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')
    return render(request, 'projects/form.html', {'form': form})

@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = projectform(instance=project)
    if request.method == 'POST':
        form = projectform(request.POST, request.FILES, instance=project)
        if form.is_valid:
            form.save()
            return redirect('projects')
    return render(request, 'projects/form.html', {'form': form})

@login_required(login_url='login')
def deleteproject(request, pk):
    profile = request.user.profile
    obj = profile.project_set.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('projects')
    return render(request, 'projects/deleteproject.html', {'obj': obj})

