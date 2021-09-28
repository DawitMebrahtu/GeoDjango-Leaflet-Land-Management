

from rest_framework import serializers
from accounts.models import *
from rest_framework_gis import serializers as geo_serializers
#class ownerSerializer(serializers.ModelSerializer):
#	class Meta:
#		model = owner
#		fields = ('user','poly', 'name','phone', 'email', 'ownership_type','date_created')


class polySerializer(geo_serializers.GeoFeatureModelSerializer):
	class Meta:
		model: poly
		fields = ('name', 'zip_code')
		geo_field="geom"

class transfer_requestSerializer(serializers.ModelSerializer):
	class Meta:
		model = transfer_request
		fields = ('owner', 'poly', 'date_created' )

