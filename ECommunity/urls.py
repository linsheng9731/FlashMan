# coding:utf8 #
__author__ = 'damon_lin'
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_article$', 'ECommunity.article_view.add_article'),
    url(r'^del_article$', 'ECommunity.article_view.del_article'),
    url(r'^update_article$', 'ECommunity.article_view.update_article'),
    url(r'^get_articles$','ECommunity.article_view.get_articles'),    
    url(r'^add_article_author$', 'ECommunity.article_view.add_article_author'),
    url(r'^del_article_author$', 'ECommunity.article_view.del_article_author'),
    url(r'^update_article_author$', 'ECommunity.article_view.update_article_author'),
    url(r'^get_article_authors$', 'ECommunity.article_view.get_article_authors'),

        
    url(r'^add_channel$', 'ECommunity.channel_view.add_channel'),
    url(r'^del_channel$', 'ECommunity.channel_view.del_channel'),
    url(r'^update_channel$', 'ECommunity.channel_view.update_channel'),
    url(r'^get_channels$','ECommunity.channel_view.get_channels'),    
    url(r'^add_channel_article$', 'ECommunity.channel_view.add_channel_article'),
    url(r'^del_channel_article$', 'ECommunity.channel_view.del_channel_article'),
    url(r'^update_channel_article$', 'ECommunity.channel_view.update_channel_article'),
    url(r'^get_channel_articles$', 'ECommunity.channel_view.get_channel_articles'),

        
    url(r'^add_collect$', 'ECommunity.collect_view.add_collect'),
    url(r'^del_collect$', 'ECommunity.collect_view.del_collect'),
    url(r'^update_collect$', 'ECommunity.collect_view.update_collect'),
    url(r'^get_collects$','ECommunity.collect_view.get_collects'),    
]