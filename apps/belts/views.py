from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    return render(request,'belts/index.html')
    #  {'everyone':User.objects.all()}
