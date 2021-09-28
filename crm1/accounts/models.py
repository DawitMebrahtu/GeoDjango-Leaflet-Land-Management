# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as gis_models
from django.db.models import Manager  


from django.contrib.auth.models import User
from django.db.models.signals import * 
# Create your models here.



#Its Model
class owner(models.Model):
	
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	
	name = models.CharField(max_length=200, null=True)

	email = models.CharField(max_length=200,null=True)
	date_created= models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name if self.name else str(self.user)



class poly(models.Model):
	owner = models.ForeignKey(owner, null=True,blank=True, on_delete= models.SET_NULL)
	name = models.CharField(max_length=200, null=True)
	ownershi=models.CharField(max_length=200, null=True, blank=True)

	visibili=models.CharField(max_length=200, null=True, blank=True)
	geom = gis_models.MultiPolygonField(null=True, geography=True)
	objects = Manager()

	def __str__(self):
		return self.name 


class transfer_request(models.Model):
	reciever = models.ForeignKey(owner, null=True, on_delete= models.SET_NULL,  related_name ='reciever')
	poly = models.ForeignKey(poly, null=True, on_delete= models.SET_NULL)
	sender = models.ForeignKey(owner, null=True, on_delete= models.SET_NULL, related_name='sender')
	date_created= models.DateTimeField(auto_now_add=True, null=True)

	
class grant_land(models.Model):
	grant_reciever  = models.ForeignKey(owner, null=True, on_delete= models.SET_NULL,  related_name ='grant_reciever')
	grant_poly = models.ForeignKey(poly, null=True, on_delete= models.SET_NULL)
	