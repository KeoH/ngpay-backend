from django.db import models

from core.behaviours import TimestampBehaviour
from merchants.models import Merchant

from .choices import API_METHODS

class APICall(TimestampBehaviour):

    method = models.CharField(max_length=6, choices=API_METHODS, default='GET')
    merchant = models.ForeignKey(Merchant, related_name="api_calls", blank=True, null=True)
    view = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.method
