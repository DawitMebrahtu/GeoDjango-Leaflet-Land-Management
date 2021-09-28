import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

#class RequestFilter(django_filters.FilterSet):
#	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
#	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
#	land = CharFilter(field_name='land', lookup_expr='icontains')
#	owner = CharFilter(field_name='land', lookup_expr='icontains')


#	class Meta:
#		model = transfer_request
#		fields = '__all__'
		#exclude = ['customer', 'date_created']