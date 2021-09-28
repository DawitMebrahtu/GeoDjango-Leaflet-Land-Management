from django.http import HttpResponse
from django.shortcuts import render, redirect


def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		
		if request.user.is_authenticated:
			return render (request, 'accounts/owner_page.html')
		else:
			return view_func(request, *args, **kwargs)
	
	return wrapper_func


def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			
			if group in allowed_roles:	
				return view_func(request, *args, **kwargs)
			else: 
				return HttpResponse('not allowed to view')

			
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'owner_team':
			return redirect('owner_page')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function

