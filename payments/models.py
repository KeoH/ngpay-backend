import uuid
from django.db import models
import django.contrib.postgres.fields as postgres_fields
from .behaviours import TimestampBehaviour


OPERATION_TYPES = (
    ('Authorization' , 'authorization'),
    ('Authorization and Capture' , 'authorization-and-capture'),
    ('Refund' , 'refund'),
    ('Void' , 'void'),
    ('Capture' , 'capture')
)

class Operation(TimestampBehaviour,models.Model):
    _db = 'payments'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=50, choices=OPERATION_TYPES)
    #description = models.TextField(verbose_name='descripción', max_length=255, blank=True, null=True)

    def last_response(self):
        return responses.objects.last()

    def __str__(self):
        return str(self.id)


class GatewayResponse(TimestampBehaviour, models.Model):
    _db = 'payments'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operation = models.ForeignKey(Operation, related_name='responses')
    status = models.CharField(verbose_name='Estado', max_length=25, default='Created', blank=True, null=True)
    response_code = models.IntegerField(verbose_name='Codigo de respuesta', default=0, blank=True, null=True)
    raw = postgres_fields.JSONField(verbose_name='Respuesta de la pasarela', default={}, blank=True, null=True)

    def __str__(self):
        return "{} : {}".format(self.operation.type, self.status)


class Payment(Operation):
    _db = 'payments'

    amount = models.DecimalField(verbose_name='Valor', max_digits=12, decimal_places=2 ,default=0.00)
