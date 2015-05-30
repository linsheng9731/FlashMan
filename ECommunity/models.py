# coding:utf8 #
__author__ = 'damon_lin'

from django.db import models

 

class user(models.Model):
	sex = models.CharField(max_length=400)
	age = models.CharField(max_length=400)
	name = models.CharField(max_length=400)
    collect = models.ManyToManyField(collect)
     channel = models.ManyToManyField(channel)
     article = models.ManyToManyField(article)
    
class article(models.Model):
    title = models.CharField(max_length=400)
    body = models.CharField(max_length=400)
    name = models.CharField(max_length=400)
    author = models.ManyToManyField(author)

 
class channel(models.Model):
    title = models.CharField(max_length=400)
    desc = models.CharField(max_length=400)
    image = models.CharField(max_length=400)
    article = models.ManyToManyField(article)

 
class collect(models.Model):
    title = models.CharField(max_length=400)
    desc = models.CharField(max_length=400)
    image = models.CharField(max_length=400)
    