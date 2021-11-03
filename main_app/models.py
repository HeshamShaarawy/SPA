from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse
from django.contrib.auth.models import User

CATEGORIES = (
    (1, 'Facial and Skin Treatments'),
    (2, 'Massage'),
    (3, 'Laser Treatments'),
    (4, 'Hand and Foot Treatments'),
    (5, 'Hair Services')
)

PAYMENTS = [
    (1, 'VISA'),
    (2, 'MASTER CARD'),
    (3, 'CRYPTO'),
    (4, 'CASH'),

]

SPECIALISTS = [
    ('Skin Care Specialist', (
        ('sk1', 'James'),
        ('sk2', 'Mary'),
    )
    ),
    ('Registered Massage Therapist', (
        ('rmt1', 'Robert'),
        ('rmt1', 'Patricia'),
    )
    ),
    ('Laser Technitian', (
        ('lsr1', 'Jennifer'),
        ('lsr2', 'Michael'),
    )
    ),
    ('Non-Registered Massage provider', (
        ('Non-RMT1', 'Pam Beesly'),
        ('Non-RMT2', 'Jim Halpert'),
    )
    ),
    ('Hair Styles', (
        ('HS-1', 'Angela Martin'),
        ('HS-2', 'Andy Bernard'),
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
    category = models.IntegerField(
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
    )
    image = models.CharField(max_length=300)
    description = models.TextField(max_length=800)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.get_category_display()} - {self.name} - ${self.price}"

    def get_absolute_url(self):
        return reverse('treatments_detail', kwargs={'treatment_id': self.id})


class Client(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=13)
    email_address = models.EmailField(max_length=254)
    payment_method = IntegerField(
        choices=PAYMENTS,
        default=[0][0]
    )
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def get_absolute_url(self):
        return reverse('clients_detail', kwargs={'client_id': self.id, 'client_name': self.last_name})


class Booking(models.Model):
    date = models.DateField()
    time = models.TimeField()
    treatment = models.ForeignKey(
        Treatment, 
        on_delete=models.CASCADE, 
    )
    specialist = models.CharField(
        choices=SPECIALISTS,
        max_length=50
    )
    status = models.IntegerField(
        choices=STATUS,
        default=STATUS[0][0]
    )
    client = models.ForeignKey(
        Client, 
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return f"{self.get_client_display()} appointment with {self.get_specialist_display()} for {self.treatment} on {self.date}: booking is {self.status}"

    def get_absolute_url(self):
        return reverse('bookings_detail', kwargs={'booking_id': self.id})
