# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.forms import inlineformset_factory

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django.views.generic.base import TemplateView

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from .filters import *

from django.contrib.gis.geos import GEOSGeometry

#for REST APIS#
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from accounts.serializers import *
from django.core.serializers import serialize


from django.contrib.auth.models import Group

from .models import *
from .forms import *
from django.contrib.gis.db.models.functions import Area


# Create your views here.


@unauthenticated_user
def registerPage(request):
	
	form = CreateUserForm()
	if request.method=='POST':
		form=CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')

	context = {'form':form}
	return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):
		
	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			if Group.objects.get(name='admin'):
				return redirect('archive')

			if Group.objects.get(name='owner_team'):
				return redirect( 'owner_page')	
		else:
			messages.info(request, 'username Or password is incorrect')
			return render(request, 'accounts/login.html')
	context = {}

	return render(request, 'accounts/login.html', context)



def logoutUser(request):
	logout(request)
	return redirect('login')






def regular(request):
	context = {}
	return render(request, 'accounts/regular.html')





@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def archive_owner(request):
	owners = owner.objects.all()
	total_owners= owners.count()
	free_land=poly.objects.filter(owner_id__isnull=True)
	owners2=owner.objects.all()
	owners_with_land = owner.objects.filter(poly__in=poly.objects.all())
	resident=owner.objects.filter(poly__in=poly.objects.filter(ownershi='residential')).count()
	corporate=owner.objects.filter(poly__in=poly.objects.filter(ownershi='corporation')).count()

	print('total ', resident)
	owners2_array=[]
	for i in owners2:
		if (i not in owners_with_land):
			owners2_array.append(i)
	print('owners2_array are',owners2_array)
	context={'land_owners':owners_with_land,'no_land_owners':owners2_array,'resident':resident,'corporate':corporate}
	return render(request, 'accounts/archive_owner.html', context) 
	
@login_required(login_url='login')
@admin_only
def archive_user(request):
	owners = owner.objects.all()
	total_owners= owners.count()
	free_land=poly.objects.filter(owner_id__isnull=True)
	owners2=owner.objects.all()
	owners_with_land = owner.objects.filter(poly__in=poly.objects.all())
	resident=owner.objects.filter(poly__in=poly.objects.filter(ownershi='residential'))
	print('total ', resident)
	owners2_array=[]
	for i in owners2:
		if (i not in owners_with_land):
			owners2_array.append(i)
	context={'no_land_owners':owners2_array}
	return render(request, 'accounts/archive_user.html', context) 
	




@login_required(login_url='login')
@admin_only
def transfer_archive(request):

	transfer_request_form = TransferForm()
	if request.method == 'POST':
		transfer_request_form= TransferForm(request.POST)
		if transfer_request_form.is_valid():
			transfer_request_form.save()
			redirect ('owner_page')

	requests1 = transfer_request.objects.all()
	
	print('requests1')
	context={'requests1': requests1, 'transfer_request_form':transfer_request_form}

	return render(request, 'accounts/transfer_archive.html', context)

@login_required(login_url='login')
@admin_only
def archive_transfer_land(request,pk):
	transfer_requests1= transfer_request.objects.get(id=pk)
	one_request=transfer_request.objects.get(id=pk)
	transfer_request_form = TransferForm(instance=one_request)
	if request.method == 'POST':
		transfer_request_form= TransferForm(request.POST, instance=one_request)
		if transfer_request_form.is_valid():
			poly.objects.filter(owner_id=one_request.sender).update(owner=one_request.reciever)
			print('request be like:',one_request.sender)
			one_request.delete()
			return redirect ('archive')

	context={'transfer_request_form': transfer_request_form}
	return render(request, 'accounts/archive_transfer_land.html', context)

@login_required(login_url='login')
@admin_only
def archive_transfer_reject(request,pk):
	one_request=transfer_request.objects.get(id=pk)
	if request.method == "POST":
		one_request.delete()
		return redirect('archive')
	context={'one_request':one_request}
	return render(request, 'accounts/archive_transfer_reject.html', context)

@login_required(login_url='login')
@admin_only
def land_list(request):
	all_lands=poly.objects.all()
	context={'all_lands':all_lands}
	return render(request, 'accounts/land_list.html', context)


def land_list_map(request, pk):

	old_poly=poly.objects.get(id=pk)
	
	context5={ 'his_land':old_poly}
	return render(request, 'accounts/land_list_map.html', context5)

@login_required(login_url='login')
@admin_only
def archive_grant_land(request):
	grant_land_form = GrantForm()
	if request.method == 'POST':
		grant_land_form= GrantForm(request.POST)
		if grant_land_form.is_valid():
			grant_land_form.save()
			redirect ('archive_owner')
	context={'grant_land_form':grant_land_form}
	return render (request,'accounts/archive_grant_land.html',context)

@login_required(login_url='login')
@admin_only
def archive_owner_info(request, pk):
	
	owners = owner.objects.get(id=pk)
	if not poly.objects.get(owner_id=pk):
		context={'owners': owners}
	else:
		old_poly=poly.objects.get(owner_id=pk)
		area_poly=poly.objects.annotate(area_=Area("geom")).get(owner_id=pk)			
		his_name=owner.objects.get(id=pk)
		context={'owners':owners, 'old_poly':old_poly, 'his_area':area_poly.area_}
	
	print('not null polys',poly.objects.exclude(owner_id__isnull=True))

	return render(request, 'accounts/archive_owner_info.html',context)


@login_required(login_url='login')
@admin_only
def archive_map(request):
	all_lands = poly.objects.all()
	all_lands_id = poly.objects.filter(owner_id__isnull=True)
	all_name= owner.objects.filter(poly__in=poly.objects.all())
#	all_lands_owners=poly.objects.all()
	print("this is your land", all_lands)


	context = {'all_lands':all_lands, 'all_name':all_name}
	return render(request, 'accounts/archive_map.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['owner_team'])
def owner_map(request):
	old_poly=poly.objects.get(owner_id=request.user.id)
	#print('coordinatessss:::: ', )
	
	his_name = request.user.owner.name
	area_poly=poly.objects.annotate(area_=Area("geom")).get(owner_id=request.user.id)	
	dimension=old_poly.geom.boundary
	
	
	coords1=old_poly.geom.coords
	coords1_str= str(coords1)
	last_coords=coords1_str.replace('(','')
	last_coords=last_coords.replace(')','')
	last_coords1=last_coords.replace(',','  |   ')
#	print ( 'dimension is',dimension)

	print('Area:', area_poly.area_)
	
	context5={ 'his_land':old_poly, 'his_name':his_name, 'his_coordinates':last_coords1,'his_area':area_poly.area_}

	return render(request, 'accounts/owner_map.html', context5)


@login_required(login_url='login')
@allowed_users(allowed_roles=['owner_team'])
def prepared_map(request):
	old_poly=poly.objects.get(owner_id=request.user.id)

	his_name=owner.objects.get(id=request.user.id)
	area_poly=poly.objects.annotate(area_=Area("geom")).get(owner_id=request.user.id)	
	coords1=old_poly.geom.coords
	coords1_str= str(coords1)
	last_coords=coords1_str.replace('(','')
	last_coords=last_coords.replace(')','')
	last_coords1=last_coords.replace(',',' |   |   ')
	print ('sheeees :',poly)
	print('Area:', area_poly.area_)

	context5={'his_land':old_poly,'his_name':his_name, 'his_coordinates':last_coords1,'his_area':area_poly.area_}

	return render(request, 'accounts/prepared_map.html',context5)

@login_required(login_url='login')
@allowed_users(allowed_roles=['owner_team'])
def land_info_owner(request):
	old_poly=poly.objects.get(owner_id=request.user.id)
	area_poly=poly.objects.annotate(area_=Area("geom")).get(owner_id=request.user.id)
	ownership_type=old_poly.ownershi
	visibility=old_poly.visibili
	context={'ownership_type':ownership_type,'visibility':visibility,'his_area':area_poly.area_}
	return render(request,'accounts/land_info_owner.html', context)
def polys_view(request):
	polys_as_geojson = serialize('geojson', poly.objects.all())
	return JsonResponse(json.loads(polys_as_geojson))


def show_land(request):
	return render(request, 'accounts/show_land.html')

def privacy(request):
	return render(request, 'accounts/privacy.html')


def draw(request):
	return render(request, 'accounts/draw.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['owner_team'])
def owner_page(request):
	owners_with_land = owner.objects.filter(poly__in=poly.objects.all())
	this_owner = owner.objects.filter(id=request.user.id)

#	if not poly.objects.get(owner_id=request.user.id):
#		print('has no land')

	#this_owner1 = owner.objects.filter(poly__in=poly.objects.filter(owner_id=request.user.id))
	#print('has no land: ', this_owner1)
#		print('ownership: ', this_owner)
#		context ={'ownership':ownership}

	for owner_with_land in owners_with_land:
		owner_with_land_str=str(owner_with_land)
		if owner_with_land_str == request.user.username:
			ownership_boolean=1
			context={'ownership_boolean': ownership_boolean}
			return render(request, 'accounts/owner_page.html', context)
			#print(owner_with_land_str, request.user.username, ownership_boolean)

	#print('owners that have land: ', owners_with_land,'	Particular Owner: ',this_owner)

	return render(request, 'accounts/owner_page.html')

#@receiver(post_save, sender=owner)
@login_required(login_url='login')
@allowed_users(allowed_roles=['owner_team'])
def transfer_owner(request):
	def get_form(self, TransferForm=None):
		form=super(transfer_owner,self).get_form(TransferForm)
		form.fields['poly'].queryset = poly.objects.filter(owner_id='17')
		return form
	transfer_request_form = TransferForm()
	if request.method == 'POST':
		transfer_request_form= TransferForm(request.POST)
		if transfer_request_form.is_valid():
			tf = transfer_request_form.save(commit=False)
			tf.sender = owner.objects.get(user=request.user)
			tf.save()
			return redirect ('owner_page')

	your_requests=transfer_request.objects.filter(sender_id = request.user.id)
	transfer_request_form1 = transfer_request.objects.all()

	context = {'your_requests': your_requests, 'transfer_request_form': transfer_request_form,'transfer_request_form1':transfer_request_form1}
	return render(request, 'accounts/transfer_owner.html', context)




def main(request):
	return render (request, 'accounts/main.html')


def map(request):
	#polygons = serialize('geojson',)
	name = request.POST.get('name')
	geom = request.POST.get('poly')

	poly_form = poly(name=name, geom=geom)
	return render(request, 'accounts/map.html')





def vision(request):
	return render(request, 'accounts/vision.html')

def socialchar(request):
	return render(request, 'accounts/socialchar.html')

def regulations(request):
	return render(request, 'accounts/regulations.html')

def physicalchar(request):
	return render(request, 'accounts/physicalchar.html')

def disclaimer(request):
	return render(request, 'accounts/disclaimer.html')

def backgroundinfo(request):
	return render(request, 'accounts/backgroundinfo.html')

def accessibility(request):
	return render(request,'accounts/accessibility.html')

def about(request):
	return render(request, 'accounts/about.html')



@login_required(login_url='login')
@admin_only
def archive(request):
	return render(request, 'accounts/archive.html')
