import uuid
from django.db import models

from core.behaviours import TimestampBehaviour

class AbstractAccount(TimestampBehaviour):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        abstract = True


class RealAccount(AbstractAccount):
    # merchant = models.ForeignKey(Merchant, related_name="accounts") <--- Cuando esté creado el modelo
    
    pass

class SandboxAccount(AbstractAccount):
    # merchant = models.ForeignKey(Merchant, related_name="sandbox_accounts") <--- Cuando esté creado el modelo
    
    pass