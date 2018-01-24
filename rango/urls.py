from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rango import views

urlpatterns = {
    url(r'^$', views.index, name='index'),
    # here "$" is a blank in the website name
    url(r'^about', views.about, name='about'),

}
#This code imports the relevant Django machinery
# for URL mappings and the views module from rango