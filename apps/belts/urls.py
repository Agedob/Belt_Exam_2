from django.conf.urls import url
from . import views 
urlpatterns = [
    url(r'^$', views.index),
    url(r'^regi', views.register),
    url(r'^travels', views.dashboard),
    url(r'^destinations', views.dest),
    url(r'^add_trip', views.add_trip),
    url(r'^logout', views.logout),
    url(r'^login', views.login),
]