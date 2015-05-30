# coding:utf8 #
__author__ = 'damon_lin'

from ECommunity.models import article,channel,
from utils import serializer
from django.http import HttpResponse
import json

                    
 
def add_channel_article(request):
    post = request.POST
    id = post['id']
    articleid=post['articleid']
    pwd = post['pwd'] # 验证预留
    channels = channel.objects.filter(id = id)
    if channels[0] == None:
        return HttpResponse('not find !')
    article = article.objects.get(id=articleid)
    channels[0].articles.add(article)
    return HttpResponse(json.dumps({'status':'ok'}))


def del_channel_article(request):
    post = request.POST
    id = post['id']
    articleid=post['articleid']
    pwd = post['pwd'] # 验证预留
    channels = channel.objects.filter(id = id)
    if channels[0] == None:
        return HttpResponse('not find !')
    article = article.objects.get(id=articleid)
    channels[0].articles.remove(article)
    return HttpResponse(json.dumps({'status':'ok'}))

# get channel article
def get_channel_articles(request):
	post = request.POST
	id = post['id']
    articles = article.objects.filter(id=id)
    article = articles[0]
	atrs=[]
    atrs.append('channel_title')
    atrs.append('channel_body')
    	json_obj = serializer.ser(article,atrs)
	return HttpResponse(json_obj)



        
 
# add channel
def add_channel(request):
    post = request.POST
    phone = post['phonenum']

   channel = channel()
   channel.save()
   
    return HttpResponse(json.dumps({'status':'ok'}))

# delete channel
def del_channel(request):
    post = request.POST
    id = post['id']
    channels = channel.objects.filter(id = id)
    if channels[0] == None:
    	return HttpResponse('not find !')
    channels[0].delete()
    return HttpResponse(json.dumps({'status':'ok'}))

def update_channel(request):
    post = request.POST
    phone = post['phonenum']
    id = post['id']
    channels = channel.objects.filter(id=id)
    channel = channels[0]
    # update
    channel = channel()
    channel.save()

    return HttpResponse(json.dumps({'status':'ok'}))


# get channel
def get_channel(request):
    post = request.POST
    id = post['id']
    channels = channel.objects.filter(id=id)
    channel = channels[0]
    atrs=[]
    atrs.append('title')
    atrs.append('desc')
    atrs.append('image')
        json_obj = serializer.ser(channel,atrs)
    return HttpResponse(json_obj)

    
