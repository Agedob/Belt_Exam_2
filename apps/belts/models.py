from __future__ import unicode_literals
from django.db import models
import bcrypt
from time import gmtime, strftime

class BlogManager(models.Manager):
    def regi_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors["name"] = "Name shouldn't be empty."
        if len(postData['username']) < 2:
            errors["username"] = "Userame shouldn't be empty."
        if len(postData['pw']) < 8:
            errors['pw'] = "Passwords must be longer."
        elif postData['pw'] != postData['cpw']:
            errors['match'] = "Your password didn't match up."
        if User.objects.filter(username = postData['username']):
            errors['exsists'] = "Invalid Username."
        if not errors:
            pass1 = bcrypt.hashpw(postData['pw'].encode(), bcrypt.gensalt())
            User.objects.create(name=postData['name'], username=postData['username'], password=pass1)
        return errors

    def login_validator(self, POSTS):
        errors = {}
        if len(POSTS['username']) < 1 or len(POSTS['pw']) < 1:
            errors['empty'] = "Fill out Login"
        if not User.objects.filter(username = POSTS['username']):
            errors['username'] = "Wrong Username/Password"
        else:
            passs = User.objects.get(username=POSTS['username'])
            if not bcrypt.checkpw(POSTS['pw'].encode(), passs.password.encode()):
                errors['passs'] = "Wrong Username/password"
        return errors
# done with log commit

    def trip_validator(self, POSTS, use_id):
        errors = {}
        a = strftime("%Y-%m-%d", gmtime())
        print POSTS['from']
        if len(POSTS['dest']) < 3 or len(POSTS['desc']) < 3:
            errors['empty'] = "Fill out form"
        if POSTS['to'] < POSTS['from']:
            errors['back to'] = "STILL NOT DOC"
        if POSTS['from'] < a:
            errors['future'] = "Your not doc"
        if not errors:
            Trip.objects.create(destination=POSTS['dest'],description=POSTS['desc'],travel_from=POSTS['from'],travel_to=POSTS['to'],user_id=use_id)
        return errors
# trip val done commit 


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BlogManager() 

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    travel_from = models.CharField(max_length=255)
    travel_to = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="user_trip")
    users = models.ManyToManyField(User, related_name="user_trips")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BlogManager() 