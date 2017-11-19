from django.db import models


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=80, null=False)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    tel = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)

    class Meta:
        ordering = ('id',)
