# coding:utf8 #
__author__ = 'damon_lin'

from ECommunity.models import collect,
from utils import serializer
from django.http import HttpResponse
import json

            
 
# add collect
def add_collect(request):
    post = request.POST
    phone = post['phonenum']

   collect = collect()
   collect.save()
   
    return HttpResponse(json.dumps({'status':'ok'}))

# delete collect
def del_collect(request):
    post = request.POST
    id = post['id']
    collects = collect.objects.filter(id = id)
    if collects[0] == None:
    	return HttpResponse('not find !')
    collects[0].delete()
    return HttpResponse(json.dumps({'status':'ok'}))

def update_collect(request):
    post = request.POST
    phone = post['phonenum']
    id = post['id']
    collects = collect.objects.filter(id=id)
    collect = collects[0]
    # update
    collect = collect()
    collect.save()

    return HttpResponse(json.dumps({'status':'ok'}))


# get collect
def get_collect(request):
    post = request.POST
    id = post['id']
    collects = collect.objects.filter(id=id)
    collect = collects[0]
    atrs=[]
    atrs.append('title')
    atrs.append('desc')
    atrs.append('image')
        json_obj = serializer.ser(collect,atrs)
    return HttpResponse(json_obj)

    
