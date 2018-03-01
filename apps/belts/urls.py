from django.conf.urls import url
from . import views 
urlpatterns = [
    url(r'^$', views.index),
    url(r'^regi', views.register),
    url(r'^travels', views.dashboard),
    url(r'^dest/(?P<num>\d+)', views.dest),
    url(r'^add_trip', views.add_trip),
    url(r'^logout', views.logout),
    url(r'^login', views.login),
    url(r'^adding_trip', views.adding_trip),
    url(r'^join/(?P<num>\d+)', views.join_trip),
]