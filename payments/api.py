
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from payments.models import Payment
from payments.serializers import PaymentSerializer

class ListPayments(generics.ListCreateAPIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
