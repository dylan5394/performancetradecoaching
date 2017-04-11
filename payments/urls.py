from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^company$', views.company, name='company'),
    url(r'^about$', views.about, name='about'),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^login$', views.loginrequest, name='loginrequest'),
    url(r'^loginform$', views.loginpage, name='loginpage'),
    url(r'^logout_request$', views.logout_request, name='logoutrequest'),
    url(r'^create_account$', views.create_account, name='createaccount'),
]