# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Account


def index(request):
    return render(request, 'payments/index.html', None)


def company(request):
    parsed = request.GET['testparam']
    return HttpResponse("At the company page with test param: %s" % parsed)


def about(request):
    return HttpResponse("At the about page")


def blog(request):
    return HttpResponse("At the blog page")


def contact(request):
    return HttpResponse("At the contact page")