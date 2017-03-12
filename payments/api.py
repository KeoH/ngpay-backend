
from rest_framework import generics

from payments.models import Payment
from payments.serializers import PaymentSerializer

class ListPayments(generics.ListCreateAPIView):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
