import uuid
from django.db import models

from core.behaviours import TimestampBehaviour
from .choices import OPERATION_TYPES
from transactions.models import Transaction

class AmountOperationBehaviour(models.Model):

    amount = models.DecimalField(verbose_name='Valor', max_digits=12, decimal_places=2 ,default=0.00)

    class Meta:
        abstract = True


class Operation(TimestampBehaviour):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.id)


class Authorization(Operation, AmountOperationBehaviour):
    
    transaction = models.ForeignKey(Transaction, related_name='authorizations')


class Capture(Operation, AmountOperationBehaviour):

    transaction = models.ForeignKey(Transaction, related_name='captures')


class AuthorizationAndCapture(Operation, AmountOperationBehaviour):

    transaction = models.ForeignKey(Transaction, related_name='authorizations_and_captures')

    class Meta:
        verbose_name_plural = 'Authorizations and Captures'
        verbose_name_plural = 'Authorizations and Captures'


class Refund(Operation, AmountOperationBehaviour):

    transaction = models.ForeignKey(Transaction, related_name='refunds')


class Void(Operation):

    transaction = models.ForeignKey(Transaction, related_name='voids')
