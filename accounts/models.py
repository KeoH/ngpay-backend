import uuid
from django.db import models

from core.behaviours import TimestampBehaviour

from merchants.models import Merchant

class AbstractAccount(TimestampBehaviour):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Account(AbstractAccount):

    merchant = models.ForeignKey(Merchant, related_name="accounts")

    def __str__(self):
        return '{} / {}'.format(self.merchant.name, 'Verified' if self.is_verified else 'Unverified')