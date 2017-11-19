from django.db import models


class Line(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80, null=False, blank=False)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    invoice = models.ForeignKey('invoices.Invoice', on_delete=models.CASCADE, null=False, related_name='lineitems')


class Meta:
    ordering = ('id',)
