from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # here "$" is a blank in the website name
    url(r'^about', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
#    url(r'^category/<category_name_slug>/add_page/$',
#        views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',
        views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
]
#This code imports the relevant Django machinery
# for URL mappings and the views module from rango