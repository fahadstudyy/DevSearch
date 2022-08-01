from django.urls import path
from projects import views

urlpatterns = [
    path('', views.projects , name='projects'),
    path('create-project/',views.create_project, name='create-project'),
    path('update-project/<str:pk>/',views.update_project, name='update-project'),
    path('project/<str:pk>/',views.project, name='project'),
    path('delete/<str:pk>/',views.deleteproject, name='deleteproject')
]