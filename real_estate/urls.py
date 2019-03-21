from django.urls import path
from .views import (
    indexPageView,
    projectsListPageView,
    projectDetailPageView,
    projectCreatePageView
)

urlpatterns = [
    path('', indexPageView, name='index'),
    path('projects-list/', projectsListPageView, name='projects_list'),
    path('project-detail/<int:pk>/', projectDetailPageView,
         name='project_detail'),
    path('project/new/', projectCreatePageView, name='project_new')
]
