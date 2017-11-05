import uuid

from django.db import models
from django.contrib.postgres import fields as postgres_fields

from core.behaviours import TimestampBehaviour
from operations.models import Operation

class Response(TimestampBehaviour):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operation = models.ForeignKey(Operation, related_name='responses')
    status = models.CharField(verbose_name='Estado', max_length=25, default='Created', blank=True, null=True)
    response_code = models.IntegerField(verbose_name='Codigo de respuesta', default=0, blank=True, null=True)
    raw = postgres_fields.JSONField(verbose_name='Respuesta', default={}, blank=True, null=True)

    def __str__(self):
        return str(self.id)
