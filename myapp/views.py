from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from myapp import *

def index(request):
    return render(request, 'index.html', {'title':'index'})

def shop(request): 
    return render(request, "shop.html") 

def about(request): 
    return render(request, "about.html") 

def services(request): 
    return render(request, "services.html") 

def blog(request): 
    return render(request, "blog.html") 

def contact(request): 
    return render(request, "contact.html") 