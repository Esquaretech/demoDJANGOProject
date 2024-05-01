from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.core.mail import send_mail
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

def cart(request):
    return render(request, "cart.html")

def checkout(request):
    return render(request, "checkout.html")

def contact_form_submit(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email
        send_mail(
            'New Contact Query',
            f'Name: {first_name} {last_name}\nEmail: {email}\nMessage: {message}',
            'esquaretech2023@gmail.com',  # Your email address
            ['esquaretech2023@gmail.com'],  # Recipient's email address
            fail_silently=False,
        )
        return HttpResponse('Query submitted successfully!')
    else:
        return HttpResponse('Method not allowed')