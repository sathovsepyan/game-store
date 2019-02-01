from django.contrib import admin

from payments.models import Payment 

class PaymentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Payment, PaymentAdmin)
