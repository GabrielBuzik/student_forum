from django.urls import path
from . import views


app_name = 'about'

urlpatterns = [
    path('project/', views.AboutProjectView.as_view(), name='project'),
    path('tech/', views.AboutTechView.as_view(), name='tech'),
]
