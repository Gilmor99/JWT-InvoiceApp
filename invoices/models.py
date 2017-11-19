from django.db import models


class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField(null=False)
    fromName = models.CharField(max_length=100, blank=False, null=False)
    billTo = models.CharField(max_length=80, blank=False, null=False)
    toAddress = models.CharField(max_length=80)
    toCity = models.CharField(max_length=80)
    toState = models.CharField(max_length=2)
    toZipcode = models.CharField(max_length=5)
    toTel = models.CharField(max_length=10)
    toFax = models.CharField(max_length=10)
    date = models.CharField(max_length=8, blank=False, null=False)
    paymentTerms = models.CharField(max_length=8, blank=False, null=False)
    dueDate = models.CharField(max_length=8, blank=False, null=False)
    balanceDue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    subTotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    taxFlag = models.CharField(max_length=1, choices=[('0', '%'), ('1', '$')])
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discountFlag = models.CharField(max_length=1, choices=[('0', '%'), ('1', '$')])
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amountPaid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, null=False, related_name='invoices')

    class Meta:
        ordering = ('id',)
