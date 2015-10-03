from django.db import models

# Create your models here.

class content(models.Model):
	text = models.CharField(max_length=300)
class tag(models.Model):
	tagname = models.CharField(max_length=300)
	content = models.ManyToManyField(content)
class user(models.Model):
	username = models.CharField(max_length=30)
	email = models.EmailField()
	tagname = models.ManyToManyField(tag)
