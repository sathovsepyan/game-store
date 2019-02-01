from django.db import models
from . import PaymentStatus


# class Order(models.Model):
#     class Meta:
#         verbose_name = 'Order'
#         verbose_name_plural = 'Orders'


class Payment(models.Model):
    sid = models.CharField(max_length=255)
    # order = models.ForeignKey(Order, related_name='orders', on_delete=models.CASCADE)
    #: Creation date and time
    created = models.DateTimeField(auto_now_add=True)
    #: Date and time of last modification
    modified = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default='0.0')
    checksum = models.CharField(max_length=255)
    status = models.CharField(max_length=10, 
        choices=PaymentStatus.CHOICES,
        default=PaymentStatus.WAITING)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ['created']
