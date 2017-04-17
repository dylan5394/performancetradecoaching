# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username


class BlogPost(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.author



