# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.utils.crypto import random

from payments.models import Account
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


def loginpage(request):
    return render(request, 'payments/login.html', None)


def loginrequest(request):
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
    code = generateActivationCode(username)
    subject = "Your new Performance Trade Coaching account."
    message = "Click the link below to verify your email: www.performancetradecoaching.com/payments/%s" % code
    from_email = "dylan5394@aim.com"
    send_mail(subject, message, from_email, ["dkdav2@gmail.com"], fail_silently=False)
    login(request, user)
    return render(request, 'payments/index.html', None)


def generateActivationCode(usernamesalt):
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    if isinstance(usernamesalt, unicode):
        usernamesalt = usernamesalt.encode('utf8')
    return hashlib.sha1(salt + usernamesalt).hexdigest()
