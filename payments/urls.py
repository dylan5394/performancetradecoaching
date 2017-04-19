from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^company$', views.company, name='company'),
    url(r'^about$', views.about, name='about'),
    url(r'^blog$', views.blog_posts, name='blog'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^login$', views.login_request, name='loginrequest'),
    url(r'^loginform$', views.login_page, name='loginpage'),
    url(r'^logout_request$', views.logout_request, name='logoutrequest'),
    url(r'^create_account$', views.create_account, name='createaccount'),
    url(r'^add_comment$', views.add_comment, name='addcomment'),
    url(r'^verify_email/(?P<code>.+)$', views.verify_email, name='verifyemail'),
]