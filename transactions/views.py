
from rest_framework.viewsets import ModelViewSet

from core.authentication import CredentialAuthentication
from transactions.models import Transaction
from .serializers import TransactionSerializer

from api.mixins import APICallsRegisterMixin

class TransactionViewSet(APICallsRegisterMixin, ModelViewSet):

    authentication_classes = [CredentialAuthentication,]
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

