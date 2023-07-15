from django.contrib import admin
from django.urls import path,re_path
from pages import views
from django.conf import settings
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap




sitemaps = {
    'static': StaticViewSitemap,
}



urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('projects',views.projects,name="projects"),
    path('contact-me',views.contact,name="contact"),
    #path('bot',views.chat_view,name="Chat Bot"),
    path('privacy-policy',views.privacy_policy,name="privacy-policy"),
    path('signup', views.signup, name="signup"),
    path('logout', views.handleLogout, name="handle_logout"),
    path('activate/<uidb64>/<slug:token>', views.activate, name='activate'),
    path('forgot_password', views.forgot_password, name="forgot_password"),
    path('reset_password/<slug:token>', views.reset_password, name="reset_password"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]



