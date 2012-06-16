# -*- coding: utf-8 -*-

from django.db import models

status_choice = (
	('a', 'activo'),
	('d', 'deshabilitado'),
	)

class Client(models.Model):
	name = models.CharField(max_length=50)
	status = models.CharField(max_length=1, default='a', choices=status_choice)
	
	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name 		= "Cliente"
		verbose_name_plural = "Clientes"
	
	def getTotalTweets(self):
		total = Tweet.objects.filter(client = self.id, category = None).count()
		return total

	#TODO:
	def getTotalClassifiedTweets(self):
		#Get all categories
		categories = TweetCategory.objects.all()

		response = []
		for category in categories:
			aux = {}
			aux['text'] = category.text
			aux['total'] = Tweet.objects.filter(client = self.id, category = category.id).count()
			response.append(aux)
		return response

class Filter(models.Model):
	client = models.ForeignKey(Client, verbose_name="Cliente")
	text = models.CharField(max_length=50)
	status = models.CharField(max_length=1, default='a', choices=status_choice)
	def __unicode__(self):
		return self.text

	class Meta:
		verbose_name 		= "Filtro"
		verbose_name_plural = "Filtros"

class TweetCategory(models.Model):
	text = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.text

	class Meta:
		verbose_name 		= "Categoria"
		verbose_name_plural = "Categorias"
	
	def getTotalTweets(self):
		return Tweet.objects.filter(category = self.id).count()

class Tweet(models.Model):
	
    author 		= models.CharField(max_length=50)
    text 		= models.CharField(max_length=140)
    date 		= models.DateTimeField()
    tweet_id	= models.CharField(max_length=20)
    client 		= models.ForeignKey(Client, verbose_name="Cliente")
    category 	= models.ForeignKey(TweetCategory, null='true', verbose_name=u"Categoría")


    class Meta:
    	unique_together = ('author','text', 'client')

    def __unicode__(self):
    	return (self.author+' : '+self.text)