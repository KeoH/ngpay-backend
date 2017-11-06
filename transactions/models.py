import uuid

from django.db import models

from core.behaviours import TimestampBehaviour
from .mixins import OperationManagerMixin


class Transaction(OperationManagerMixin, TimestampBehaviour):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    

    def __str__(self):
        return str(self.id)


