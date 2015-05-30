# coding:utf8 #
__author__ = 'damon_lin'

from ECommunity.models import article,channel,collect,user,
from utils import serializer
from django.http import HttpResponse
import json

                                    
 
def add_user_article(request):
    post = request.POST
    id = post['id']
    articleid=post['articleid']
    pwd = post['pwd'] # 验证预留
    users = user.objects.filter(id = id)
    if users[0] == None:
        return HttpResponse('not find !')
    article = article.objects.get(id=articleid)
    users[0].articles.add(article)
    return HttpResponse(json.dumps({'status':'ok'}))


def del_user_article(request):
    post = request.POST
    id = post['id']
    articleid=post['articleid']
    pwd = post['pwd'] # 验证预留
    users = user.objects.filter(id = id)
    if users[0] == None:
        return HttpResponse('not find !')
    article = article.objects.get(id=articleid)
    users[0].articles.remove(article)
    return HttpResponse(json.dumps({'status':'ok'}))

# get user article
def get_user_articles(request):
	post = request.POST
	id = post['id']
    articles = article.objects.filter(id=id)
    article = articles[0]
	atrs=[]
    atrs.append('user_title')
    atrs.append('user_body')
    	json_obj = serializer.ser(article,atrs)
	return HttpResponse(json_obj)



        
 
def add_user_channel(request):
    post = request.POST
    id = post['id']
    channelid=post['channelid']
    pwd = post['pwd'] # 验证预留
    users = user.objects.filter(id = id)
    if users[0] == None:
        return HttpResponse('not find !')
    channel = channel.objects.get(id=channelid)
    users[0].channels.add(channel)
    return HttpResponse(json.dumps({'status':'ok'}))


def del_user_channel(request):
    post = request.POST
    id = post['id']
    channelid=post['channelid']
    pwd = post['pwd'] # 验证预留
    users = user.objects.filter(id = id)
    if users[0] == None:
        return HttpResponse('not find !')
    channel = channel.objects.get(id=channelid)
    users[0].channels.remove(channel)
    return HttpResponse(json.dumps({'status':'ok'}))

# get user channel
def get_user_channels(request):
	post = request.POST
	id = post['id']
    channels = channel.objects.filter(id=id)
    channel = channels[0]
	atrs=[]
    atrs.append('user_title')
    atrs.append('user_desc')
    	json_obj = serializer.ser(channel,atrs)
	return HttpResponse(json_obj)



        
 
def add_user_collect(request):
    post = request.POST
    id = post['id']
    collectid=post['collectid']
    pwd = post['pwd'] # 验证预留
    users = user.objects.filter(id = id)
    if users[0] == None:
        return HttpResponse('not find !')
    collect = collect.objects.get(id=collectid)
    users[0].collects.add(collect)
    return HttpResponse(json.dumps({'status':'ok'}))


def del_user_collect(request):
    post = request.POST
    id = post['id']
    collectid=post['collectid']
    pwd = post['pwd'] # 验证预留
    users = user.objects.filter(id = id)
    if users[0] == None:
        return HttpResponse('not find !')
    collect = collect.objects.get(id=collectid)
    users[0].collects.remove(collect)
    return HttpResponse(json.dumps({'status':'ok'}))

# get user collect
def get_user_collects(request):
	post = request.POST
	id = post['id']
    collects = collect.objects.filter(id=id)
    collect = collects[0]
	atrs=[]
    atrs.append('desc')
    atrs.append('image')
    	json_obj = serializer.ser(collect,atrs)
	return HttpResponse(json_obj)



        
 
# add user
def add_user(request):
    post = request.POST
    phone = post['phonenum']

   user = user()
   user.save()
   
    return HttpResponse(json.dumps({'status':'ok'}))

# delete user
def del_user(request):
    post = request.POST
    id = post['id']
    users = user.objects.filter(id = id)
    if users[0] == None:
    	return HttpResponse('not find !')
    users[0].delete()
    return HttpResponse(json.dumps({'status':'ok'}))

def update_user(request):
    post = request.POST
    phone = post['phonenum']
    id = post['id']
    users = user.objects.filter(id=id)
    user = users[0]
    # update
    user = user()
    user.save()

    return HttpResponse(json.dumps({'status':'ok'}))


# get user
def get_user(request):
    post = request.POST
    id = post['id']
    users = user.objects.filter(id=id)
    user = users[0]
    atrs=[]
    atrs.append('sex')
    atrs.append('age')
    atrs.append('name')
        json_obj = serializer.ser(user,atrs)
    return HttpResponse(json_obj)

    
