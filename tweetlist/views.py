from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from tweetlist.models import Client, Filter, TweetCategory, Tweet
import subprocess
import os
import sys

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers

clients 	= Client.objects.filter(status = 'a')
categories 	= TweetCategory.objects.all()

def index(request):
	tweets = Tweet.objects.order_by('-date')
	return showListOfTweets(request, tweets)

def tweetsByClient(request, client_id):
	tweets = Tweet.objects.filter(client = client_id, category = None).order_by('-date')
	return showListOfTweets(request, tweets, client_id)

def showListOfTweets(request, tweets, client_id = '', tweet_category_id = ''):
	paginator = Paginator(tweets, 8) # Muestra 8 tweets por pagina
	page = request.GET.get('page')

	try:
		tweets = paginator.page(page)
	except PageNotAnInteger:
		tweets = paginator.page(1)
	except EmptyPage:
		tweets = paginator.page(paginator.num_pages)

	if client_id != '':
		return render_to_response('tweetlist/client_tweetlist.html', 
			{'clients': clients, 'tweets':tweets, 'categories':categories, 'client_id': int(client_id)},
	                               context_instance=RequestContext(request))
	else:
		return render_to_response('tweetlist/index.html', 
			{'clients': clients, 'tweets':tweets, 'categories':categories, 'client_id': ''},
	                               context_instance=RequestContext(request))

#Reports
def tweetsReport(request, client_id):
	c = Client.objects.get(id=client_id)
	categories_pk = categories.values('pk').query

	#TODO: Evitar tweet descartados
	abs_stats = {}
	abs_total = Tweet.objects.filter(client=client_id, category__in=categories_pk).count()
	for category in categories:
		if category.text != "Descartado":
			abs_stats[category.text] = Tweet.objects.filter(client=client_id, category=category.id).count()

	return render_to_response('tweetlist/report.html', 
		{'clients':clients, 'c':c, 'categories':categories, 'abs_total':abs_total, 'abs_stats':abs_stats},
                               context_instance=RequestContext(request))

#AJAX
def changeTweetCategory(request, tweet_id, category_id):
	tweet 		= Tweet.objects.get(pk=tweet_id)
	category 	= TweetCategory(id=category_id)

	#TODO: Comprobar tweet y category por si no existiesen y devolver error en tal caso.

	tweet.category = category
	response = ""
	tweet.save()

	tweet = Tweet.objects.get(pk=tweet_id)
	if tweet.category.id == int(category_id):
		response = "true"
	else:
		response = "false"

	return HttpResponse(response)

def getTweetsFromTwitter(request):
	command = "python "+os.path.join(os.path.dirname(__file__), '../daemon.py').replace('\\','/')
	os.system(command)

	return HttpResponse(command)