from django.conf.urls import patterns, include, url
from hello_world import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'),
                           url(r'^about', views.about, name='about'),
                           url(r'^better/$', views.better_hello, name='better'),
)