from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import ListeningResource
import random
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
import json
from .tokens import account_activation_token
from django.db import IntegrityError

def search_view(request):
    if request.method=="POST":
	    title = request.POST.get('search-title')
	    if title!="":
		    results = ListeningResource.objects.filter(title__icontains=title)
		    context = {
		    'title': title,
		    'results':results,
		    }
			    
    
    
    return render(request, 'search_results.html', context)

def check_user(request):
	if request.method=='POST':
	    username = request.POST.get('data_field')
	    data = {
	    'is_available':User.objects.filter(username=username).exists()
	    }
	    return JsonResponse(data)
	    
	    
# req functions
def activate(request, uidb64, token):
    try:
	    decoded_str = force_str(urlsafe_base64_decode(uidb64))  # Convert bytes to a strin
	    if decoded_str!="":
		    uid = int(decoded_str)
		    user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        login(request,user)
        return redirect('home')
    else:
        messages.error(request, 'Activation link is invalid!')
    
    return redirect('home')

def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.content_subtype='html'
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to your email <b>{to_email}</b> inbox and click on \
            the received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending a confirmation email to {to_email}, check if you typed it correctly.')

def handleSignup(request, form_data):
    # Get the post parameters
    username = form_data.get('username')
    email = form_data.get('email')
    fname = form_data.get('fname')
    lname = form_data.get('lname')
    pass1 = form_data.get('pass1')
    pass2 = form_data.get('pass2')

    if len(username) > 10:
        messages.error(request, 'Your username must be under 10 characters')
        return redirect('home')

    if username.isalnum() == False:
        messages.error(request, 'Username should only contain letters and numbers')
        return redirect('home')

    if pass1 != pass2:
        messages.error(request, 'Passwords do not match')
        return redirect('home')

    try:
	    myuser = User.objects.create_user(username, email, pass1)
	    myuser.first_name = fname
	    myuser.last_name = lname
	    myuser.is_active = False
	    myuser.save()
	    user = myuser
	    
	    activateEmail(request, user, email)
	    return redirect('home')
    except IntegrityError:
        messages.error(request, 'User with this user name already exists')
    except:
        messages.error(request, 'Some error occurred')




def handleLogin(request, form_data):
    username = form_data.get('loginUsername')
    password = form_data.get('loginPassword')

    user = authenticate(username=username, password=password)
    userr = User.objects.get(username=username)
    if userr is not None:
	    if not userr.is_active:
		    activateEmail(request,userr,userr.email)
		    return redirect('home')
	    else:
		    if user is not None:
			    login(request, user)
			    messages.success(request, 'Successfully Logged In')
			    return redirect('home')
		    else:
			    messages.error(request, 'Invalid crenditials!')
			    return redirect('signup')
    else:
        messages.error(request, 'No user found with this username! If you are not registered please signup')
        return redirect('signup')


# Create your views here.

def home(request):
	return render(request, 'index.html')


def about(request):
    return render(request, 'sorry.html')


def services(request):
    return render(request, 'sorry.html')


def projects(request):
    return render(request, 'sorry.html')


def contact(request):
    return render(request, 'sorry.html')
    
def privacy_policy(request):
	return render(request, 'privacy-policy.html')


def signup(request):
    if request.user.is_authenticated:
    	messages.error(request, "You're already logged in.")
    	return redirect('home')

    if request.method == 'POST':
        form_data = request.POST
        if 'signup' in form_data:
            handleSignup(request, form_data)
        elif 'login' in form_data:
            handleLogin(request, form_data)

    return render(request, 'signup.html')


def forgot_password(request):
    return render(request, 'forgot.html')


def reset_password(request, token):
    return render(request, 'reset.html')


def handleLogout(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('home')


def handling_404(request, exception):
    return render(request, '404.html', {})
    
def handling_500(request, exception):
    return render(request, '500.html', {})
    
def send_email(subject,message,to):
	email = EmailMessage(mail_subject, message, to)
	email.content_subtype='html'