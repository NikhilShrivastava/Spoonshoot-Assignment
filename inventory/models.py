# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    bookId = models.CharField(max_length=100 , blank=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __self__(self):
        return self.name
