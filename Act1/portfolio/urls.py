from django.urls import path
from .views import index, contact, about, projects

app_name = "portfolio"

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('projects', projects, name='projects'),
]
