import uuid
from django.db import models
from django.contrib.auth.models import User
from core.behaviours import TimestampBehaviour

class Merchant(TimestampBehaviour):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    fiscal_code = models.CharField(max_length=50, null=True, blank=True)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.name