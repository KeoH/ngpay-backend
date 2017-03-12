from django.contrib import admin
from django.contrib.postgres.fields import JSONField

from prettyjson import PrettyJSONWidget

from .models import Payment, GatewayResponse

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'creation_date', 'type', 'amount']


class GatewayResponseAdmin(admin.ModelAdmin):
    list_display = ['operation', 'creation_date', 'status', 'response_code']
    formfield_overrides = {
        JSONField : {
            'widget' : PrettyJSONWidget
        }
    }


admin.site.register(Payment, PaymentAdmin)
admin.site.register(GatewayResponse, GatewayResponseAdmin)
