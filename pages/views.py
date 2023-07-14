#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import ChatMessage
import random
import requests


# req functions

def handleSignup(request, form_data):
    # Get the post parameters
    username = form_data.get('username')
    email = form_data.get('email')
    fname = form_data.get('fname')
    lname = form_data.get('lname')
    pass1 = form_data.get('pass1')
    pass2 = form_data.get('pass2')

    # check for erroneous input
    '''if any(x in "" for x in [username,email,fname,lname,pass1,pass2]):
    	messages.error(request,'Please fill out all the boxes')
    	return redirect("signup")
    '''
    if len(username) > 10:
        messages.error(request, 'Your username must be under 10 characters')
        return redirect('home')

    if username.isalnum() == False:
        messages.error(request, 'Username should only contain letters and numbers')
        return redirect('home')
    if pass1 != pass2:
        messages.error(request, 'Passwords do not match')
        return redirect('home')

    # Create the user
    myuser = User.objects.create_user(username, email, pass1)
    myuser.first_name = fname
    myuser.last_name = lname
    myuser.save()
    messages.success(request, 'Your account has been successfully created')
    return redirect('signup')


def handleLogin(request, form_data):
    username = form_data.get('loginUsername')
    password = form_data.get('loginPassword')

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, 'Successfully Logged In')
        return redirect('home')
    else:
        messages.error(request, 'Invalid credentials! Please try again.')
        return redirect('home')


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'sorry.html')


def services(request):
    return render(request, 'sorry.html')


def projects(request):
    return render(request, 'sorry.html')


def contact(request):
    return render(request, 'sorry.html')


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

"""
@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        response = process_message(message)
        chat_message = ChatMessage.objects.create(message=message, reply=response)
        chat_messages = ChatMessage.objects.values('message').distinct()
        
        data = []
        for chat_message in chat_messages:
            data.append({'message': chat_message['message'], 'reply': ChatMessage.objects.filter(message=chat_message['message']).last().reply})
        
        return JsonResponse({'chat_messages': data})
    
    return render(request, 'chat.html')

def process_message(message):
    if any(x in message.lower() for x in ['hi','hlo','hello','whats up','whatsup','sup']):
        response = "Hello there!"
    elif any(x in message.lower() for x in ['bye','exit','goodbye','goodnight']):
        response = "Goodbye!"
    else:
        responses = ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm still learning."]
        response = random.choice(responses)
    return response
"""