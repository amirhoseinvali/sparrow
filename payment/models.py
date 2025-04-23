from django.db import models

class Payment(models.Model):
    order = models.OneToOneField('orders.Order', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    gateway = models.CharField(max_length=50)  # زرین‌پال، IDPay و ...
    transaction_id = models.CharField(max_length=100)
    status = models.CharField(max_length=20)  # موفق، ناموفق، در انتظار
    created_at = models.DateTimeField(auto_now_add=True)