from django.urls import path
#from django.conf.urls import url
from django.conf.urls import *
from . import views
from accounts.models import *
from django.views.generic import TemplateView
from accounts.views import polys_view


urlpatterns = [

   	path('archive/', views.archive, name="archive"),
	path('owner_page/', views.owner_page, name="owner_page"),


	path('owner_map/', views.owner_map, name='owner_map'),
	path('archive_map/', views.archive_map, name='archive_map'),
	path('polys.data/', polys_view, name='polys'),
	#url('show_land/', views.show_land, name='show_land'),
   	path('register/', views.registerPage, name="register"),
   	path('login/', views.loginPage, name="login"),
   	path('archive_owner/', views.archive_owner, name="archive_owner"),
   	path('main/', views.main),
   	path('privacy/', views.privacy, name="privacy"),

   	path('map/', views.map, name="map"),


   	path('draw/', views.draw, name="draw"),
   	path('transfer_owner/', views.transfer_owner, name='transfer_owner'),
   	path('owner_page/', views.owner_page, name="owner_page"),
   	path('regular/', views.regular, name="regular"),
   	path('prepared_map/', views.prepared_map, name="prepared_map"),
   	path('land_info_owner/', views.land_info_owner, name="land_info_owner"),
 
   	path('about/', views.about, name="about"),
   	path('accessibility/', views.accessibility, name="accessibility"),
   	path('backgroundinfo/', views.backgroundinfo, name="backgroundinfo"),
   	path('disclaimer/', views.disclaimer, name="disclaimer"),
   	path('physicalchar/', views.physicalchar, name="physicalchar"),
   	path('regulations/', views.regulations, name="regulations"),
   	path('socialchar/', views.socialchar, name="socialchar"),
   	path('vision/',views.vision, name="vision"),
   	
   	path('transfer_archive/', views.transfer_archive, name='transfer_archive'),

	path('archive_owner_info/<str:pk>/', views.archive_owner_info, name='archive_owner_info'),
	
	path('archive_transfer_land/<str:pk>/', views.archive_transfer_land, name='archive_transfer_land'),   	
	path('archive_transfer_reject/<str:pk>/', views.archive_transfer_reject, name='archive_transfer_reject'),   	
		
	path('archive_grant_land/', views.archive_grant_land, name='archive_grant_land'),   	
	path('archive_user/', views.archive_user, name="archive_user"),
	path('land_list/', views.land_list, name="land_list"),
	path('land_list_map/<str:pk>/', views.land_list_map, name="land_list_map"),


   	path('logout/', views.logoutUser, name="logout"),
   
	
	 
]