from django.db import models
from django_markdown.models import MarkdownField
# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length = 200)
	body = MarkdownField()
	pub_date = models.DateField('Publice date')
	support = models.IntegerField()
	def __str__(self):
		return self.title
class Comment(models.Model):
	article = models.ForeignKey(Article)
	username = models.CharField(max_length = 200)
	body = MarkdownField()
	pub_date = models.DateField('Comment Publice date')
	def __str__(self):
		return self.username
