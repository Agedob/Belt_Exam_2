from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    return render(request,'belts/index.html', {'everyone':User.objects.all()})

def dashboard(request):
    if not "id" in request.session:
        messages.error(request, "Login")
        return redirect('/')
    else:
        me = User.objects.get(id = request.session['id'])
        content = {'mytrips': me.user_trip.all(),
        'sometrips':me.user_trips.all(),
        'alltrips':Trip.objects.all().exclude(users=request.session['id']).exclude(user=request.session['id'])}
    return render(request,'belts/travel.html',content)

def dest(request,num):
    if not "id" in request.session:
        messages.error(request, "Login")
        return redirect('/')
    else:
        x = Trip.objects.get(id = num)
        content = {"user":x.user,"trip":x,"joining":x.users.all()}
    return render(request,'belts/destination.html', content)

def add_trip(request):
    if not "id" in request.session:
        messages.error(request, "Login")
        return redirect('/')
    else:
        return render(request,'belts/add_trip.html')

def logout(request):
    request.session.clear()
    return redirect('/')

def register(request):
    if request.method != 'POST':
        messages.error(request, "Create User")
        return redirect('/')
    else:
        errors = User.objects.regi_validator(request.POST)
        if len(errors):
            for key,values in errors.iteritems():
                messages.success(request, values)
            return redirect('/')
        else:
            id = User.objects.get(username=request.POST['username']).id
            request.session['id'] = id
            request.session['name'] = request.POST['name']
            return redirect('/travels')

def login(request):
    if request.method != 'POST':
        messages.error(request, "Create User")
        return redirect('/')
    else:
        errors = User.objects.login_validator(request.POST)
        if len(errors):
            for key,values in errors.iteritems():
                messages.success(request, values)
            return redirect('/')
        else:
            id = User.objects.get(username=request.POST['username']).id
            name = User.objects.get(username=request.POST['username']).name
            request.session['id'] = id
            request.session['name'] = name
        return redirect('/travels')

def adding_trip(request):
    if request.method != 'POST':
        messages.error(request, "Create User")
        return redirect('/')
    else:
        errors = Trip.objects.trip_validator(request.POST,request.session['id'])
        if len(errors):
            for key,values in errors.iteritems():
                messages.success(request, values)
            return redirect('/add_trip')
        else:
            return redirect('/travels')

def join_trip(request,num):
    if not "id" in request.session:
        messages.error(request, "Login")
        return redirect('/')
    else:
        id = User.objects.get(id = request.session['id'])
        tid = Trip.objects.get(id=num)
        tid.users.add(id)
        print "worked"
        return redirect('/travels')