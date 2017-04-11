# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


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

