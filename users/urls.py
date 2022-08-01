from django.urls import path
from . import views
urlpatterns = [
    path('', views.profile, name="profile"),
    path('Logout/', views.logoutuser, name="logout"),

    path('Profile/<str:pk>/', views.userProfile, name="userprofile"),
    path('Login/', views.loginuser, name="login"),
    path('Register/', views.registeruser, name="register"),
    path('Account/', views.userAccount, name="account"),
    path('EditAccount/', views.editAccount, name="editaccount"),
    path('SkillForm/', views.CreateSkill, name="skillform"),
    path('EditSkill/<str:pk>/', views.UpdateSkill, name="editskill"),
    path('deleteSkill/<str:pk>/', views.DeletetSkill, name="deleteskill"),
    
]
