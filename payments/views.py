# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import hashlib

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.utils.crypto import random
from django.utils import timezone
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

    date = datetime.datetime.now() + datetime.timedelta(days=2)
    format_string = "%Y-%m-%d %H:%M:%S"
    code = generate_activation_code(username)
    expires = datetime.datetime.strftime(date, format_string)
    user = Account.objects.create_user(username, email, password, activation_code=code, code_expires=expires)
    user.is_active = False
    user.save()

    subject = "Your new Performance Trade Coaching account."
    message = "Click the link below to verify your email: www.performancetradecoaching.com/payments/verify_email/%s" % code
    from_email = "dylan5394@aim.com"
    send_mail(subject, message, from_email, ["dkdav2@gmail.com"], fail_silently=False)
    return render(request, 'payments/index.html', None)


def generate_activation_code(username_salt):
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    if isinstance(username_salt, unicode):
        username_salt = username_salt.encode('utf8')
    return hashlib.sha1(salt + username_salt).hexdigest()


def verify_email(request, code):
    user = get_object_or_404(Account, activation_code=code)
    if not user.is_active:
        if timezone.now() > user.code_expires:
            print("Expired") #TODO: Show error page here
        else:
            print("Activating user account")
            user.is_active = True
            user.save()
            login(request, user)
    else:
        print("Code already used") #TODO: Show error page here
    return render(request, 'payments/index.html', None)


def blog_posts(request):
    posts = BlogPost.objects.all()
    return render(request, 'payments/blogs.html', {'posts': posts})


def blog_post(request, blog_id):
    post = BlogPost.objects.get(id=blog_id)
    return render(request, 'payments/blog.html', {'post': post})


def add_comment(request):
    author = request.user
    body = request.POST['body']
    blog_id = request.POST['blog_id']
    parent = BlogPost.objects.get(id=blog_id)
    comment = Comment(author=author, body=body, post=parent)
    comment.save()
