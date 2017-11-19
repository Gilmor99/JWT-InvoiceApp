from rest_framework import serializers
from lineitems.models import Line
from invoices.models import Invoice
from invoices.serializers import InvoiceSerializer
from rest_framework.serializers import ValidationError


class LineSerializer(serializers.ModelSerializer):

    invoice = InvoiceSerializer(read_only=True)
    invoice_id = serializers.PrimaryKeyRelatedField(
        queryset=Invoice.objects.all(), source='invoice')
    def validate(self, data):
        """
        Validating the amount claculation
        """
        try:
            data['amount'] = data['quantity'] * data['rate']
        except ValidationError:
            raise serializers.ValidationError("Quantity and Rate need to be positvie decimal numbers")
        return data

    class Meta:
        model = Line
        fields = ('id', 'description', 'quantity', 'rate', 'amount', 'invoice', 'invoice_id')
        read_only_fields = ('amount',)
