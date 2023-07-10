from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
	return render(request,'index.html')
	
def about(request):
	return render(request,'sorry.html')
	
def services(request):
	return render(request,'sorry.html')
	
def projects(request):
	return render(request,'sorry.html')
	
def contact(request):
	return render(request,'sorry.html')
	
	
if not settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
    ]