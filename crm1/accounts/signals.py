from django.contrib.auth.models import User
from django.db.models.signals import * 
from accounts.models import *
from django.contrib.auth.models import Group

def owner_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='owner_team')
		instance.groups.add(group)

		owner.objects.create(
			user=instance,
			name=instance.username,
			email=instance.email,
			id=instance.id,
			)

post_save.connect(owner_profile, sender=User)




def poly_transfer_owner(sender,instance, **kwargs):
		transfer_request5= transfer_request.objects.all()
		instance.id = instance.sender_id
		owner5= owner.objects.all()
		sender5=owner.objects.get(id=instance.id)
		reciever5=owner.objects.get(id=instance.reciever_id)
		print('sender: ', sender5)
		print('reciever :',reciever5)
		print('request:  :',instance.id)
pre_save.connect(poly_transfer_owner, sender=transfer_request)


def grant_land_signal_pre(sender, instance,**kwargs):
	instance.id=instance.grant_reciever.id
pre_save.connect(grant_land_signal_pre,sender=grant_land)

def grant_land_signal_post(sender,instance,**kwargs):
	free_poly=poly.objects.filter(owner_id__isnull=True)
	if (instance.grant_poly in free_poly):
		poly.objects.filter(id=instance.grant_poly.id).update(owner=instance.grant_reciever)
		print('It  is free and it is:', instance.grant_poly)
	print ('sssssssssss', instance.grant_reciever.id,'rrrrrrr',instance.id)
post_save.connect(grant_land_signal_post, sender=grant_land)


