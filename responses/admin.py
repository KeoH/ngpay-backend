from django.contrib import admin
from django.contrib.postgres.fields import JSONField

from prettyjson import PrettyJSONWidget

from responses.models import Response


class ResponseAdmin(admin.ModelAdmin):
    list_display = ['operation', 'creation_date', 'status', 'response_code']
    formfield_overrides = {
        JSONField : {
            'widget' : PrettyJSONWidget
        }
    }


admin.site.register(Response, ResponseAdmin)

