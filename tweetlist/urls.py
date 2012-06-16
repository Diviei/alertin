from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('tweetlist.views',
    url(r'^$', 'index'),
    url(r'^client\/(?P<client_id>\d+)/$', 'tweetsByClient'),

    #Informes
    url(r'^report\/(?P<client_id>\d+)/$', 'tweetsReport'),

    #AJAX
    url(r'^ajax\/changeTweetCategory\/(?P<tweet_id>\d+)\/(?P<category_id>\d+)/$', 'changeTweetCategory'),
    url(r'^ajax\/getTweetsFromTwitter/$', 'getTweetsFromTwitter'),
)

urlpatterns += staticfiles_urlpatterns()