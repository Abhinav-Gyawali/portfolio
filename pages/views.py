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