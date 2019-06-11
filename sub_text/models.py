from django.db import models
from django.contrib.auth.models import User

class student(models.Model):
	name = models.CharField(max_length=40)
	email = models.CharField(max_length=40)
	password = models.CharField(max_length=40)
	city = models.CharField(max_length=40)
	marks = models.IntegerField()
	favorite_fruit = models.CharField(max_length=40)
	countries =models.CharField(max_length=40)
	fruits = models.CharField(max_length=40)
	docfile = models.FileField()
	def __str__(self):
		return self.user.username



class signup(models.Model):
	username = models.CharField(max_length=100)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	email =  models.CharField(max_length=100)
	password = models.CharField(max_length=100)


	def __str__(self):
		return self.username


class products(models.Model):
	pid = models.CharField(max_length=40)
	pname = models.CharField(max_length=40)
	pprice = models.CharField(max_length=40)
	pimage = models.FileField()

	def __str__(self):
		return self.pid

class userrecord(models.Model):
	uid = models.CharField(max_length=40)
	pid = models.CharField(max_length=40)
	pname = models.CharField(max_length=40)
	pprice = models.CharField(max_length=40)
	pimage = models.FileField()

	def __str__(self):
		return self.uid



class contact(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	email = models.EmailField(max_length=50)
	message = models.CharField(max_length=250)

	def __str__(self):
		return self.name