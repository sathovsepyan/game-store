from django.utils.translation import pgettext_lazy

class PaymentStatus:
    WAITING = 'waiting'
    CONFIRMED = 'confirmed'
    REJECTED = 'rejected'
    ERROR = 'error'

    CHOICES = [
        (WAITING, pgettext_lazy('payment status', 'Waiting for confirmation')),
        (CONFIRMED, pgettext_lazy('payment status', 'Confirmed')),
        (REJECTED, pgettext_lazy('payment status', 'Rejected')),
        (ERROR, pgettext_lazy('payment status', 'Error'))]