from django.db import models
from django.db.models.fields import IntegerField


# Create your models here.


CATEGORIES = (
    (1, 'Facial and Skin Treatments'),
    (2, 'Massage'),
    (3, 'Lazer Treatments'),
    (4, 'Hand and Foot Treatments'),
    (5, 'Hair Services')
)

PAYMETS = [
    (1, 'VISA'),
    (2, 'MASTER CARD'),
    (3, 'CRYPTO'),
    (4, 'CASH'),

]


class Treatment(models.Model):
    name = models.CharField(max_length=100)
    category = IntegerField(
        choices=CATEGORIES,
        default=[1][0]
    )
    image = models.CharField(max_length=300)
    description = models.TextField(max_length=800)
    price = models.DecimalField(max_digits=7, decimal_places=2)


class Client(models.Model):
    name = models.CharField(max_length=300)
    phone_number = models.IntegerField(max_length=13)
    email_address = models.EmailField(max_length=254)
    credit_card = IntegerField(max_length=20)
