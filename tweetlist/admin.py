from tweetlist.models import Tweet
from tweetlist.models import Filter
from tweetlist.models import Client
from tweetlist.models import TweetCategory
from django.contrib import admin

class TweetAdmin(admin.ModelAdmin):
    fields 			= ['client', 'author', 'text', 'date', 'tweet_id']
    list_display 	= ('date','author', 'text', 'client', 'category')
    date_hierarchy 	= 'date'
    list_filter 	= ['date','client','category']
    search_fields 	= ['text']
    ordering       	= ('-date',)

admin.site.register(Client)
admin.site.register(Filter)
admin.site.register(TweetCategory)
admin.site.register(Tweet, TweetAdmin)