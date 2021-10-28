from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse


# Create your models here.


CATEGORIES = (
    (1, 'Facial and Skin Treatments'),
    (2, 'Massage'),
    (3, 'Laser Treatments'),
    (4, 'Hand and Foot Treatments'),
    (5, 'Hair Services')
)

PAYMETS = [
    (1, 'VISA'),
    (2, 'MASTER CARD'),
    (3, 'CRYPTO'),
    (4, 'CASH'),

]

SPECIALISTS = [
    ('Skin Care Specialist', (
        ('sk1', 'Skin1'),
        ('sk2', 'Skin2'),
    )
    ),
    ('Registered Massage Therapist', (
        ('rmt1', 'Reg.M.T.1'),
        ('rmt1', 'Reg.M.T.2'),
    )
    ),
    ('Laser Technitian', (
        ('lsr1', 'Laser 1'),
        ('lsr2', 'Laser 2'),
    )
    ),
    ('Non-Registered Massage provider', (
        ('Non-RMT1', 'Non-1'),
        ('Non-RMT2', 'Non-2'),
    )
    ),
    ('Hair Styles', (
        ('HS-1', 'Hair Artist -1'),
        ('HS-2', 'Hair Artist -2'),
    )
    ),
    ('any', 'any'),
]

STATUS = (
    (1, 'Scheduled'),
    (2, 'Performed'),
    (3, 'Cancelled')
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
    def __str__(self):
        return f"{self.name} - {self.get_category_display()} - ${self.price}"
    def get_absolute_url(self):
        return reverse('treatments_detail', kwargs={'treatment_id': self.id})


class Client(models.Model):
    name = models.CharField(max_length=300)
    phone_number = models.IntegerField(max_length=13)
    email_address = models.EmailField(max_length=254)
    payment_method = IntegerField(
        choices=PAYMETS,
        default=[0][0]
    )




class Booking(models.Model):
    date = models.DateTimeField()
    specialist = models.CharField(
        choices=SPECIALISTS,
        max_length=50
    )
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    client = models.CharField(
        default='Client Name',
        max_length=100
    )
    status = models.IntegerField(
        choices=STATUS,
        default=STATUS[0][0]
    )

    def __str__(self):
        return f"{self.client} appointment with {self.get_specialist_display()} for {self.treatment} on {self.date}: booking is {self.status}"

    def get_absolute_url(self):
        return reverse('bookings_detail', kwargs={'booking_id': self.id})
