# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Account, BlogPost, Comment

# Register your models here.
admin.site.register(Account)
admin.site.register(BlogPost)
admin.site.register(Comment)