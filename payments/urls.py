from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^company$', views.company, name='company'),
    url(r'^about$', views.about, name='about'),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^contact$', views.contact, name='contact'),
]