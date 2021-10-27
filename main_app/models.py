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

class Treatment(models.Model):
    name = models.CharField(max_length=100)
    category = IntegerField(
        choices=CATEGORIES,
        default=[1][0]
    )
    image = models.CharField(max_length=300)
    description = models.TextField(max_length=800)
    price = models.DecimalField(max_digits=7, decimal_places=2)

