from django.contrib import admin
from django.urls import path,re_path
from pages import views
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('projects',views.projects,name="projects"),
    path('contact-me',views.contact,name="contact"),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]