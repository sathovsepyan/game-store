from django.db import models
from orders.models import Order

class Payment(models.Model):
    STATUS = [
        ('waiting', 'Waiting'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
        ('error', 'Error')
    ]
    sid = models.CharField(max_length=255)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    #: Creation date and time
    created = models.DateTimeField(auto_now_add=True)
    #: Date and time of last modification
    modified = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default='0.0')
    checksum = models.CharField(max_length=255)
    status = models.CharField(max_length=10, 
        choices=STATUS,
        default=STATUS[0])

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ['created']
