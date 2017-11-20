from rest_framework import serializers
from accounts.models import Account
from invoices.models import Invoice


class AccountSerializer(serializers.ModelSerializer):
    '''
    Define the Account's serializer and its associated linked invoices
    '''
    invoices = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=False,
        queryset=Invoice.objects.all(),
        view_name='invoice-detail',
    )

    class Meta:
        model = Account
        fields = ('url', 'id', 'company', 'address', 'city', 'state', 'zipcode', 'tel', 'fax', 'invoices')
