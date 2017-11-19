from accounts.models import Account
from rest_framework import viewsets
from accounts.serializers import AccountSerializer
from rest_framework import permissions


class AccountViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
