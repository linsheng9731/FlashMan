# coding:utf8 #
__author__ = 'damon_lin'

from ECommunity.models import author,article,
from utils import serializer
from django.http import HttpResponse
import json

                    
 
def add_article_author(request):
    post = request.POST
    id = post['id']
    authorid=post['authorid']
    pwd = post['pwd'] # 验证预留
    articles = article.objects.filter(id = id)
    if articles[0] == None:
        return HttpResponse('not find !')
    author = author.objects.get(id=authorid)
    articles[0].authors.add(author)
    return HttpResponse(json.dumps({'status':'ok'}))


def del_article_author(request):
    post = request.POST
    id = post['id']
    authorid=post['authorid']
    pwd = post['pwd'] # 验证预留
    articles = article.objects.filter(id = id)
    if articles[0] == None:
        return HttpResponse('not find !')
    author = author.objects.get(id=authorid)
    articles[0].authors.remove(author)
    return HttpResponse(json.dumps({'status':'ok'}))

# get article author
def get_article_authors(request):
	post = request.POST
	id = post['id']
    authors = author.objects.filter(id=id)
    author = authors[0]
	atrs=[]
    atrs.append('article_name')
    atrs.append('article_gender')
    	json_obj = serializer.ser(author,atrs)
	return HttpResponse(json_obj)



        
 
# add article
def add_article(request):
    post = request.POST
    phone = post['phonenum']

   article = article()
   article.save()
   
    return HttpResponse(json.dumps({'status':'ok'}))

# delete article
def del_article(request):
    post = request.POST
    id = post['id']
    articles = article.objects.filter(id = id)
    if articles[0] == None:
    	return HttpResponse('not find !')
    articles[0].delete()
    return HttpResponse(json.dumps({'status':'ok'}))

def update_article(request):
    post = request.POST
    phone = post['phonenum']
    id = post['id']
    articles = article.objects.filter(id=id)
    article = articles[0]
    # update
    article = article()
    article.save()

    return HttpResponse(json.dumps({'status':'ok'}))


# get article
def get_article(request):
    post = request.POST
    id = post['id']
    articles = article.objects.filter(id=id)
    article = articles[0]
    atrs=[]
    atrs.append('title')
    atrs.append('body')
    atrs.append('name')
        json_obj = serializer.ser(article,atrs)
    return HttpResponse(json_obj)

    
