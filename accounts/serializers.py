from rest_framework import serializers
from accounts.models import Account
from invoices.models import Invoice


class AccountSerializer(serializers.ModelSerializer):
    invoices = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=False,
        queryset=Invoice.objects.all(),
        view_name='invoice-detail',
    )

    class Meta:
        model = Account
        fields = ('url', 'id', 'company', 'address', 'city', 'state', 'zipcode', 'tel', 'fax', 'invoices')
