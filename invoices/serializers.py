from rest_framework import serializers
from invoices.models import Invoice
from accounts.models import Account
from lineitems.models import Line
from accounts.serializers import AccountSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    account_id = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), source='account')

    lineitems = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=False,
        queryset=Line.objects.all(),
        view_name='line-detail',
    )

    def validate(self, data):
        """
        Calculate the subTotal, Total and Ballance Due amounts
        """

        data['subTotal'] = 0
        for line in data['lineitems']:
            data['subTotal'] = data['subTotal'] + line.amount
        if data['subTotal'] > 0:
            if data['taxFlag'] == 0:
                tax = data['subTotal'] * data['tax']
            else:
                tax = data['tax']
            if data['discountFlag'] == 0:
                discount = data['subTotal'] * data['discount']
            else:
                discount = data['discount']
            data['total'] = data['subTotal'] + tax - discount + data['shipping']
            data['balanceDue'] = data['total'] - data['amountPaid']
        return data

    class Meta:
        model = Invoice
        fields = ('id', 'number', 'fromName', 'billTo', 'date', 'paymentTerms', 'dueDate', 'balanceDue', 'subTotal', 'taxFlag', 'tax', 'discountFlag', 'discount', 'shipping', 'total', 'amountPaid', 'account', 'account_id', 'toAddress', 'toCity', 'toState', 'toZipcode', 'toTel', 'toFax', 'lineitems')
        read_only_fields = ('subTotal', 'total', 'balanceDue')
