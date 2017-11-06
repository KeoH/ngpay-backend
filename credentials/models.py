import uuid
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from core.behaviours import TimestampBehaviour
from accounts.models import Account

from .choices import CREDENTIALS_TYPES

class Credential(TimestampBehaviour):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    credential_type = models.CharField(max_length=10, choices=CREDENTIALS_TYPES, default="sandbox")
    account = models.ForeignKey(Account, related_name="credentials")

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def success_login(self, username, password):
        return username+password == self.username+self.password

    def __str__(self):
        return '{} / {} / {}'.format(self.account.merchant.name, self.credential_type,'Verified' if self.account.is_verified else 'Unverified')