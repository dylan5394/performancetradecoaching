# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Account, BlogPost

# Register your models here.
admin.site.register(Account)
admin.site.register(BlogPost)
