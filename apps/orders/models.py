from django.db import models
from django.contrib.auth.models import User
import uuid

class Order(models.Model):
    STATUS = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('error', 'Error'),
    ]
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, default='0.0')
    status = models.CharField(max_length=10, 
        choices=STATUS,
        default=STATUS[0])

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

