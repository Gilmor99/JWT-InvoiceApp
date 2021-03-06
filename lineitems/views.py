from lineitems.models import Line
from rest_framework.viewsets import ModelViewSet
from lineitems.serializers import LineSerializer
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework import permissions


class LineViewSet(NestedViewSetMixin, ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    model = Line
    queryset = Line.objects.all()
    serializer_class = LineSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
