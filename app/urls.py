from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('projects',views.projects,name="projects"),
    path('contact-me',views.contact,name="contact"),
    path('search',views.search_view,name="search_view"),
    path('privacy-policy',views.privacy_policy,name="privacy-policy"),
    path('signup', views.signup, name="signup"),
    path('logout', views.handleLogout, name="handle_logout"),
    path('activate/<uidb64>/<slug:token>', views.activate, name='activate'),
    path('forgot_password', views.forgot_password, name="forgot_password"),
    path('reset_password/<slug:token>', views.reset_password, name="reset_password"),
    path('check_user/', views.check_user, name='check_user'),
]