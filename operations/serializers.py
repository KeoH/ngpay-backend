
from rest_framework import serializers

from operations.models import Payment

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = [ 'id', 'type', 'amount', 'creation_date' ]
