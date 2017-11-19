from invoices.models import Invoice
from rest_framework.viewsets import ModelViewSet
from invoices.serializers import InvoiceSerializer
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework import permissions


class InvoiceViewSet(NestedViewSetMixin, ModelViewSet):
    model = Invoice
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
