from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Profile
from .models import Skill as skilling
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import *
def loginuser(request):
    page = 'register'
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request,'WRONG USERNAME OR PASSOWRD')
    return render(request, 'users/login_create.html')

def registeruser(request):
    form = CutsomUserForm()
    page = 'register'

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User created succesfully')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_create.html', context)

def logoutuser(request):
    logout(request)
    messages.error(request,'User does not exist')
    return redirect('login')

def profile(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    skills = skilling.objects.filter(name__iexact=search_query)

    obj = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skill__in= skills)
        )
    return render(request, 'users/profile.html', {'profiles': obj})

def userProfile(request, pk):
    obj = Profile.objects.get(id=pk)
    topskills = obj.skill_set.exclude(descreption__exact="")
    skills = obj.skill_set.filter(descreption = "")
    context = {'profile': obj, 'skills':topskills, 'skill':skills}
    return render(request, 'users/user_profile.html', context)

@login_required(login_url='login')
def userAccount (request):
    profile = request.user.profile
    topskills = profile.skill_set.exclude(descreption__exact="")
    skills = profile.skill_set.filter(descreption = "")
    context = {'profile': profile, 'skills':topskills, 'skill':skills}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount (request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/editaccount.html', context)

def CreateSkill(request):
    profile = request.user.profile
    form = Skill()
    if request.method == 'POST':
        form = Skill(request.POST)
        if form.is_valid:            
            skill = form.save(commit = False)
            skill.owner = profile
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/skill_form.html' ,context)

def UpdateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = Skill(instance=skill)
    if request.method == 'POST':
        form = Skill(request.POST, instance=skill)
        if form.is_valid:
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/skill_form.html' ,context)

def DeletetSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('account')
    context = {'skill':skill}
    return render(request, 'users/delete_skill.html', context)