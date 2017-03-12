
from rest_framework import serializers

from payments.models import Payment

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = [ 'id', 'type', 'description', 'amount', 'creation_date' ]
