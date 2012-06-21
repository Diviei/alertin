#!/usr/bin/eval PYTHONPATH=/home/diviei/modules python
#Standar libraries
import os
import sys
from datetime import datetime

#django libraries
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alertin.settings")
from tweetlist.models import Tweet
from tweetlist.models import Filter
from tweetlist.models import Client

#Twitter library
import twitter

api = twitter.Api()

"""
def GetSearch(self,
                term=None,
                geocode=None,
                since_id=None,
                per_page=15,
                page=1,
                lang="sp",
                show_user="true",
                query_users=False):
"""

#TODO: Coger lista de palabras
words = Filter.objects.all()

#Coger resultado de las palabras
for word in words:
	results = api.GetSearch(word.text, None, None, 1000, 1, 'es')
	client_id = word.client_id

	for result in results:
		text 		= result.GetText()
		username 	= result.GetUser().GetScreenName()
		date 		= datetime.fromtimestamp(result.GetCreatedAtInSeconds())
		tweet_id 	= result.GetId()
		
		try:
			t = Tweet(None)
			t.author 	= username
			t.text 		= text
			t.date 		= date
			t.client_id = client_id
			t.tweet_id 	= tweet_id
			t.save()
		except Exception, e:
			print e