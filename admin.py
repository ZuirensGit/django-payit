from django.contrib import admin
from .models import Spgateway
# Register your models here.



class SpgatewayAdmin(admin.ModelAdmin):
	list_display = ('merchant_id', 'merchant_name', 'member_name', 'manager_name', 'manager_mobile')
	readonly_fields = ('business_type', 'merchant_type', 'credit_autotype', 'credit_limit', 'payment_type', 'agreed_day', 'agreed_fee')



admin.site.register(Spgateway, SpgatewayAdmin)