# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.utils.crypto import random
from payments.models import Account, BlogPost, Comment
from django.core.mail import send_mail


def index(request):
    return render(request, 'payments/index.html', None)


def company(request):
    return render(request, 'payments/company.html', None)


def about(request):
    return render(request, 'payments/about.html', None)


def blog(request):
    return render(request, 'payments/blog.html', None)


def contact(request):
    return render(request, 'payments/contact.html', None)


def login_page(request):
    return render(request, 'payments/login.html', None)


def login_request(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'payments/index.html', None)
    else:
        return HttpResponse("Could not login")


def logout_request(request):
    logout(request)
    return render(request, 'payments/index.html', None)


def create_account(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = Account.objects.create_user(username, email, password)
    code = generate_activation_code(username)
    subject = "Your new Performance Trade Coaching account."
    message = "Click the link below to verify your email: www.performancetradecoaching.com/payments/%s" % code
    from_email = "dylan5394@aim.com"
    send_mail(subject, message, from_email, ["dkdav2@gmail.com"], fail_silently=False)
    login(request, user)
    return render(request, 'payments/index.html', None)


def generate_activation_code(username_salt):
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    if isinstance(username_salt, unicode):
        username_salt = username_salt.encode('utf8')
    return hashlib.sha1(salt + username_salt).hexdigest()


def blog_posts(request):
    posts = BlogPost.objects.all()
    return render(request, 'payments/blog.html', {'posts': posts})


def add_comment(request):
    author = request.POST['author']
    body = request.POST['body']
    blog_id = request.POST['blog-id']
    parent = BlogPost.objects.get(id=blog_id)
    comment = Comment(author=author, body=body, post=parent)
    comment.save()
