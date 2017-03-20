from django.contrib import admin
from .models import Spgateway
# Register your models here.



class SpgatewayAdmin(admin.ModelAdmin):
    list_display = ('check_api', 'merchant_id', 'merchant_name', 'member_name', 'manager_name', 'manager_mobile')
    readonly_fields = ('business_type', 'merchant_type', 'credit_autotype', 'credit_limit', 'payment_type', 'agreed_day', 'agreed_fee')
    list_display_links = ('merchant_id',)

    def check_api(self,obj):
        return u'<button class="%s" id="payment">%s</button>' % (obj.status, obj.status)
    check_api.allow_tags = True
    check_api.short_description = "API Check"


admin.site.register(Spgateway, SpgatewayAdmin)