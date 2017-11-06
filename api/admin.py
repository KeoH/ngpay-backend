from django.contrib import admin

from .models import APICall

class ApiCallAdmin(admin.ModelAdmin):
    list_display = ['method', 'view','creation_date']

admin.site.register(APICall, ApiCallAdmin)