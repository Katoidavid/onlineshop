from django.db import models
from datetime import date


class Customer(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    KENYA_COUNTIES = [
        ('Nairobi', 'Nairobi'),
        ('Mombasa', 'Mombasa'),
        # Add more counties as needed
    ]

    image = models.ImageField(upload_to='customer_images/', blank=True)
    name = models.CharField(max_length=20)
    admissionNumber = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField(max_length=25)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    county = models.CharField(max_length=100, choices=KENYA_COUNTIES)
    date_of_birth = models.DateField()
    age = models.PositiveIntegerField(null=True, blank=True)  # Field to store age

    def save(self, *args, **kwargs):
        # Calculate age based on date_of_birth
        if self.date_of_birth:
            today = date.today()
            self.age = today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
