from django.contrib import admin

from .models import Authorization, AuthorizationAndCapture, Capture, Refund, Void

admin.site.register(Authorization)
admin.site.register(AuthorizationAndCapture)
admin.site.register(Capture)
admin.site.register(Refund)
admin.site.register(Void)