# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_auto_20171117_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='company',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='amountPaid',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='balanceDue',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='billTo',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subTotal',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='tax',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
