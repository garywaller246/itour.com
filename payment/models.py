from django.db import models
from booking.models import Booking


class Payment(models.Model):
	METHOD = (
        ('credit', 'Credit card'),
        ('debit', 'Debit card'),
        ('paypal', 'PayPal'),
    )

	booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	method = models.CharField(max_length=20, choices=METHOD,
								default='credit')
	card_name = models.CharField(max_length=100)
	card_number = models.IntegerField()
	card_date = models.CharField(max_length=5)
	card_cvv = models.IntegerField()