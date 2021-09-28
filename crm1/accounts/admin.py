# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from leaflet.admin import LeafletGeoAdminMixin
from leaflet_admin_list.admin import LeafletAdminListMixin
from django.contrib import admin
from django.contrib.gis import admin

from leaflet.admin import LeafletGeoAdmin
# Register your models here.
from .models import *

admin.site.register(owner)



#admin.site.register(plot)

admin.site.register(transfer_request)
admin.site.register(grant_land)

#admin.site.register(poly)
class polyAdmin(LeafletGeoAdmin):
	map_template = ('accounts/map.html')
	#editor_deselector : "vWKTField"
	list_display = ("name", "geom")


admin.site.register(poly, polyAdmin)