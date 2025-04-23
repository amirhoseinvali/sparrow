from django.db import models

class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_type = models.CharField(max_length=10, choices=[('percent', 'Percentage'), ('fixed', 'Fixed Amount')])
    discount_value = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    max_usage = models.PositiveIntegerField(default=1)
    used_by = models.ManyToManyField('accounts.User', blank=True)