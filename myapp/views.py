from django.shortcuts import render
from myapp import *
# Create your views here.
def index(request):
    return render(request,"index.html", {})