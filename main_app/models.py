from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse

CATEGORIES = (
    (1, 'Facial and Skin Treatments'),
    (2, 'Massage'),
    (3, 'Lazer Treatments'),
    (4, 'Hand and Foot Treatments'),
    (5, 'Hair Services')
)

class Treatment(models.Model):
    name = models.CharField(max_length=100)
    category = models.IntegerField(
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
    )
    image = models.CharField(max_length=300)
    description = models.TextField(max_length=800)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.get_category_display()} - ${self.price}"

    def get_absolute_url(self):
        return reverse('treatments_detail', kwargs={ 'treatment_id': self.id })

